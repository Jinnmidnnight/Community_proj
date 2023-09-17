from django.db import models
from django.db.models.fields import CharField, TextField
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Community(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='Community', null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Community, related_name = 'comments', on_delete = models.CASCADE, null = True)
    댓글 = models.CharField(max_length = 200)
    created_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def approve(self):
        self.save()
    
    def __str__(self):
        return self.댓글
