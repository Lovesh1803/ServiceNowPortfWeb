from django.contrib import admin
from .models import Blog, Objective, Product, Level, Role, Skill, Comment

admin.site.register(Objective)
admin.site.register(Product)
admin.site.register(Level)
admin.site.register(Role)
admin.site.register(Skill)
admin.site.register(Comment)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ['objectives', 'products', 'levels', 'roles', 'skills']
