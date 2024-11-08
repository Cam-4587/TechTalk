from django import forms
from .models import Comment, Reply, Post, Tag


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

        labels = {
            'content': 'Comment:'
        }

        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 4, 
                'cols': 70, 
                'placeholder': 'Enter Your Comment'
            })
        }

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['content']
        labels = {
            'content': 'Enter Reply here:'
        }
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 2, 
                'cols': 10,
            })
        }

class CreateBlogPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'tags', 'intro',  'intro', 'content']
        
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'image': forms.ClearableFileInput(attrs={ "class": "form-control", "id": "formFile", "label": "Default file input example"}),
            'tags': forms.SelectMultiple(attrs={ "class": "form-select", "aria-label": "Default select example"}),
            'intro': forms.Textarea(attrs={"class": "form-control"}),
            'content': forms.Textarea(attrs={"class": "form-control"}),
        }
        
        labels = {
            'tags': 'Tags, hold down ctrl to select multiple tags:'
        }
        
        