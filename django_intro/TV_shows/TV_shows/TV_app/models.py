from django.db import models
from datetime import datetime
import re


class ShowManager(models.Manager):
    def validator(self, data):
        errors = {}
        if len(data['title']) < 2:
            errors['title'] = "Title must be at least 2 characters"
        if len(data['network']) < 2:
            errors['network'] = "Network must be at least 2 characters"
        if data['release_date'] == '':
            errors['release_date'] = "Date cannot be empty"
        else:
            if datetime.strptime(data['release_date'], '%Y-%m-%d') > datetime.today():
                errors['release_date'] = "date cannot be in the future"
        print(errors)
        return errors


class Shows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=45)
    release_date = models.DateTimeField()
    desc = models.TextField(default="prev show", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
