from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Choice(models.Model):
    title = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='choice_pictures', blank=True, null=True)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    preparation = models.TextField(max_length=1000, default='')
    def get_absolute_url(self):
        return reverse('choices-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title