from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(default="old book", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'


class author(models.Model):
    name = models.CharField(max_length=255)
    notes = models.TextField(default="prev author", null=True)
    books = models.ManyToManyField(Book, related_name="publishers")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'
