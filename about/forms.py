from django import forms
from django.contrib.auth.models import User
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Profile


class UpdateProfileForm(forms.ModelForm):
    """
    Form to alter user's profile
    """
    model = Profile

    widgets = {
        'bio': CKEditorUploadingWidget(
                attrs={"class": "form-control"}, 
            ),
    }

    class Meta:
        model = Profile
        fields = ['image', 'bio']
