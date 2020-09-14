from django.db import models
from django.contrib.auth.models import User

class Home(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(default=' ')
    image = models.FileField(upload_to='images/')
    link = models.CharField(max_length=100)
    def __str__(self):
        return self.title
