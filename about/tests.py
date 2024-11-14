from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
from .forms import UpdateProfileForm
from .models import Profile


# Create your tests here.

# # form test
class UpdateProfileFormTest(TestCase):
    file=SimpleUploadedFile('file.jpg', b"file_content", content_type='image/jpeg')
    def test_form_is_valid(self):
        
        form_files = {
            'image': self.file
        }
        
        form_data = {
            'bio': 'This is the bio for my profile'
        }
        updateprofileform = UpdateProfileForm(data=form_data, files=form_files)
        self.assertTrue(updateprofileform.is_valid(), msg="Form is invalid")




