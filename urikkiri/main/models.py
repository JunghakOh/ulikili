from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

# Create your models here.
class Content(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)
    body = models.TextField(default='')
    file = models.FileField(upload_to='documents/%Y, %m/', blank=True)

class Comment(models.Model):
    objects = models.Manager()
    post = models.ForeignKey('Content', on_delete=models.CASCADE)
    text = models.TextField(default='')
    created_date = models.DateTimeField(default=timezone.now)

class Answer(models.Model):
    post = models.ForeignKey('main.Content', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text