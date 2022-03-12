from django.contrib import admin
from .models import Post
from .models import Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'author')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)