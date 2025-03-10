from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UpdateProfileForm(forms.ModelForm):
    """
    Form to alter user's profile
    """
    model = Profile

    widgets = {
        
    }

    class Meta:
        model = Profile
        fields = ['image', 'bio']
