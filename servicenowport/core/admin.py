from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, PasswordResetToken

@admin.register(User)
class CustomerAdmin(BaseUserAdmin):
    """
    Admin for Customer users only (non-staff).
    Shows only non-staff users and customizes the form to include phone.
    """
    # Display fields in the list view
    list_display = ['email', 'username', 'phone', 'is_active']
    list_filter = ['is_active']
    search_fields = ['email', 'username']
    ordering = ['email']

    # Include custom phone field in both add and change forms
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Customer Info', {'fields': ('phone',)}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Customer Info', {'fields': ('phone',)}),
    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Only show non-staff users as "customers"
        return qs.filter(is_staff=False)


@admin.register(PasswordResetToken)
class PasswordResetTokenAdmin(admin.ModelAdmin):
    """Admin for password reset tokens."""
    list_display = ['user', 'token', 'created_at', 'used', 'is_valid_display']
    list_filter = ['used', 'created_at']
    search_fields = ['user__email', 'token']

    def is_valid_display(self, obj):
        return obj.is_valid()
    is_valid_display.boolean = True
    is_valid_display.short_description = 'Valid'
