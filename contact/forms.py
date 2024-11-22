from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Contact form
    """
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
