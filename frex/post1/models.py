from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post1(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.FileField(upload_to='images/')
    content1 = models.TextField(default=' ')
    code1 = models.TextField(default=' ')
    content2 = models.TextField(default=' ')
    code2 = models.TextField(default=' ')
    video = models.FileField(upload_to='video/')
    time = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title
class Coment1(models.Model):
    name = models.ForeignKey(Post1, on_delete=models.CASCADE)
    coment = models.CharField(max_length=500)
    time = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.coment
