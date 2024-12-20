from django import forms
from django.contrib.auth.models import User
from django_summernote.widgets import SummernoteInplaceWidget
from .models import Profile


class UpdateProfileForm(forms.ModelForm):
    """
    Form to alter user's profile
    """
    model = Profile

    widgets = {
        'bio': SummernoteInplaceWidget(attrs={"class": "form-control"}),
    }

    class Meta:
        model = Profile
        fields = ['image', 'bio']
