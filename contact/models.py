from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Contact(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='message', null=True
    )
    name = models.CharField(max_length=255, blank=False, null=True)
    email = models.EmailField(max_length=254, blank=False)
    message = models.TextField(blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.user}"
