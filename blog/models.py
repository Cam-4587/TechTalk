from django.db import models
from django.contrib.auth.models import User


# Create your models here.
STATUS = ((0, "Pending Review"), (1, "Published"))

class Post(models.Model):
       title = models.CharField(max_length=200, unique=True)
       slug = models.SlugField(max_length=200, unique=True)
       author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts") 
       image = models.ImageField(upload_to='upload/', blank=True, null=True)
       intro = models.TextField(blank=True)
       content = models.TextField()
       published_date = models.DateTimeField(auto_now_add=True)
       created_on = models.DateTimeField(auto_now_add=True)
       updated_on = models.DateTimeField(auto_now=True)
       status = models.IntegerField(choices=STATUS, default=0)
       
       class Meta:
        ordering = ["-created_on"]

       def __str__(self):
        return f"{self.title} | {self.author}"
       
