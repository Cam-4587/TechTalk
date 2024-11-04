from django import forms
from .models import Comment, Reply


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