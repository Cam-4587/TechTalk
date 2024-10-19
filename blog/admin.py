from django.contrib import admin
from .models import Post, Comment, Tag

# Register your models here.

class TagAdmin(admin.ModelAdmin):
    model = Tag
    prepopulated_fields = {'slug': ('tag',)}
    
class CommentItemInline(admin.TabularInline):
    model = Comment
    extra = 1
    
class PostAdmin(admin.ModelAdmin):
    model = Post
    inlines = [CommentItemInline]
    prepopulated_fields = {'slug': ('title',)}



admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Tag,TagAdmin)