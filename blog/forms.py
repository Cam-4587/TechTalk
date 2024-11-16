from django import forms
from django_summernote.widgets import SummernoteInplaceWidget
from django.core.exceptions import ValidationError
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
            'tags': forms.SelectMultiple(attrs={ "class": "form-select multi-select"}),
            'intro': forms.Textarea(attrs={"class": "form-control", 'rows': 2,'cols': 10,}),
            'content': SummernoteInplaceWidget(attrs={"class": "form-control"}),
        }
        
        labels = {
            'tags': 'Select a maximum of 5 tags for your post:'
        }
        
    def clean_tags(self):
        tn = self.cleaned_data.get('tags')
        if not tn:  
            tn = []
        if len(tn) > 5:
            raise ValidationError('Invalid number of tags', code='invalid')
        return tn

        