from django.db import models
from django.contrib.auth.models import User


class Photos(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png',blank=True)
    owner = models.ForeignKey(User, default= None)

    def __str__(self):
      return self.title

    def snippet(self):
        return self.body[:30] + '...'