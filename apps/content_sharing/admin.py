from django.contrib import admin
from .models import Category, Content, Comment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'content_type', 'category', 'created_at', 'get_likes_count', 'comments_count')
    list_filter = ('content_type', 'category', 'created_at')
    search_fields = ('title', 'description', 'author__username')
    readonly_fields = ('created_at', 'updated_at', 'get_likes_count', 'comments_count')
    
    def get_likes_count(self, obj):
        return obj.likes.count()
    get_likes_count.short_description = 'Beğeni Sayısı'
    get_likes_count.boolean = False
    get_likes_count.admin_order_field = 'likes'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('text', 'author__username', 'content__title')