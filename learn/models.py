from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title =  models.CharField(max_length=250)
    content =  models.TextField()
    image =  models.ImageField(upload_to='post_images/', blank=True, null=True)
    author = models.CharField(max_length=100, default = "Nupur")
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete= models.CASCADE) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    email = models.EmailField()
    data_posted = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)
    def __str__(self):
        return f'Comment by {self.user.username} on "{self.post.title}"'   