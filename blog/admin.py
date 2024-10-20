from django.contrib import admin
from .models import Post, Comment, Tag, Reply

# Register your models here.

class CommentItemInline(admin.TabularInline):
    model = Comment
    extra = 1
class ReplyItemInline(admin.TabularInline):
    model = Reply
    extra = 1
class TagAdmin(admin.ModelAdmin):
    model = Tag
    prepopulated_fields = {'slug': ('tag',)}
    
class CommentAdmin(admin.ModelAdmin):
    model = Comment
    inlines = [ReplyItemInline]
    
class CommentItemInline(admin.TabularInline):
    model = Comment
    extra = 1
    
class PostAdmin(admin.ModelAdmin):
    model = Post
    inlines = [CommentItemInline]
    prepopulated_fields = {'slug': ('title',)}



admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Reply)
admin.site.register(Tag,TagAdmin)