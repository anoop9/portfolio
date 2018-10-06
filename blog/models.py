from django.db import models
from django.db.models.functions import datetime


class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=200)
    image = models.ImageField(upload_to='images/blog')
    pub_date = models.DateTimeField()

    def summary(self):
        return self.body[:100]

    def __str__(self):
        return self.title
