from django.contrib import admin
from .models import Post, Comment
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    search_fields = ['text', 'created_by']
    list_filter = ('created_by',)
    list_display = ['created_by', 'text', 'created_at']


class CommentAdmin(admin.ModelAdmin):
    search_fields = ['text', 'post']
    list_filter = ('created_by', 'post')
    list_display = ['created_by', 'text', 'post']


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
