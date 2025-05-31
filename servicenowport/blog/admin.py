from django.contrib import admin
from .models import (
    Blog, Level, Role, Comment,
    ChallengeType, CertificationPractice, ContentType, Status, Category
)

# Register new models
admin.site.register(Level)
admin.site.register(Role)
admin.site.register(Comment)
admin.site.register(ChallengeType)
admin.site.register(CertificationPractice)
admin.site.register(ContentType)
admin.site.register(Status)
admin.site.register(Category)

# Blog admin config
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = [
        'levels',
        'roles',
        'challenge_types',
        'certification_practices',
        'content_types',
        'statuses',
    ]
