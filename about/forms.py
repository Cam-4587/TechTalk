from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UpdateProfileForm(forms.ModelForm):
    model = Profile
    
    class Meta:
        model = Profile
        fields = ['image', 'bio']