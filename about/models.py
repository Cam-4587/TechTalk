from django.db import models
from django.contrib.auth.models import User
from django_summernote.fields import SummernoteTextField
from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile_name")
    image = CloudinaryField('image', default='nobody', blank=True, null=True)
    bio = SummernoteTextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
            return str(self.user)