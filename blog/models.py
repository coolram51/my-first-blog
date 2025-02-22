from django.db import models
from django.utils import timezone
""" This page define different models required in the page

class Post(models.Model):
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    text=models.TextField()
    created_date=models.DateTimeField(blank=True,null=True)
    published_date=models.DateTimeField(blank=True,null=True)
    def publish(self):
         self.published_date=timezone.now()
         self.save()
    def __str__(self):
         return self.title

# Create your models here.
