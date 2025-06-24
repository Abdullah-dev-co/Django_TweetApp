from django.contrib import admin
from .models import Tweet
from django.utils.html import format_html

class TweetAdmin(admin.ModelAdmin):
    list_display = ('user', 'truncated_content', 'created_at', 'image_preview')
    list_filter = ('created_at', 'user')
    search_fields = ('content', 'user__username')
    readonly_fields = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    
    fieldsets = (
        (None, {
            'fields': ('user', 'content', 'image')
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def truncated_content(self, obj):
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content
    truncated_content.short_description = 'Content'
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 50px; max-width: 50px;" />', obj.image.url)
        return "-"
    image_preview.short_description = 'Preview'

admin.site.register(Tweet, TweetAdmin)
