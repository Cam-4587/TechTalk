from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import UpdateProfileForm
from .models import Profile


# Create your tests here.

# form test
class UpdateProfileFormTest(TestCase):
    """Test for successful Profile form submission """

    file = SimpleUploadedFile(
        'file.jpg', b"file_content", content_type='image/jpeg'
    )

    def test_form_is_valid(self):
        form_files = {
            'image': self.file
        }
        form_data = {
            'bio': 'This is the bio for my profile'
        }
        updateprofileform = UpdateProfileForm(data=form_data, files=form_files)
        self.assertTrue(updateprofileform.is_valid(), msg="Form is invalid")


# view test
class UpdateFormViewTest(TestCase):
    """ User instance creating for testing views """

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="User",
            password="userPassword",
            email="user@test.com"
        )

    def test_successful_profile_update(self):
        """Test for updating profile and redirecting back to profile page """

        self.client.login(username="User", password="userPassword")
        profile_data = {'bio': "Updated Profile bio"}
        url = reverse('update-profile')
        response = self.client.post(url, profile_data)
        self.assertRedirects(response, "/about/profile/", 302)

    def test_successful_profile_delete(self):
        """
        Test for deleting profile and redirecting back to user's profile page
        """

        profile = Profile()
        self.client.login(username="User", password="userPassword")
        url = reverse('delete-profile')
        response = self.client.post(url)
        self.assertRedirects(response, "/about/profile/", 302)
        self.assertEqual(profile.bio, "")
        self.assertEqual(profile.image, "nobody")
