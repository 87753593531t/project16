from django.contrib import admin
from posts.models import Post, Comment, PostLike


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'comment')

admin.site.register(Comment, CommentAdmin)
admin.site.register(Post)
admin.site.register(PostLike)

# Register your models here.
