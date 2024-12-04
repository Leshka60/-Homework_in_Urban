from django.contrib import admin
from .models import Category, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'is_published')
    search_fields = ('title', 'content')
    list_filter = ('category', 'created_at')
    list_per_page = 5

    fieldsets = (
        (None, {'fields': ('title', 'content', 'category')}),
        ('Дополнительные настройки', {
            'classes': ('collapse',),
            'fields': ('created_at', 'is_published', 'updated_at')
        }),
    )

    readonly_fields = ('created_at', 'updated_at')
