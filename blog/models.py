from django.db import models
from django.contrib.auth.models import User


# Create your models here.
STATUS = ((0, "Pending Review"), (1, "Published"))

class Tag(models.Model):
       tag = models.CharField(max_length=20, unique=True)
       slug = models.SlugField(max_length=20, unique=True)
       
       def __str__(self):
        return f"{self.tag}"

class Post(models.Model):
       title = models.CharField(max_length=200, unique=True)
       slug = models.SlugField(max_length=200, unique=True)
       tags = models.ManyToManyField(Tag)
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

class Comment(models.Model):
       post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
       author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
       content= models.TextField()
       approved = models.BooleanField(default=False)
       created_on = models.DateTimeField(auto_now_add=True)
       
       class Meta:
        ordering = ["-created_on"]
        
       def __str__(self):
         return f"{self.author} | {self.post}"
       
