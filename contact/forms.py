from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Contact form
    """
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 100%;'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'style': 'width: 100%;'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'style': 'width: 100%;'}),
        }

