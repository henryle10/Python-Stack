from django.db import models


class Dojo(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=30)
    desc = models.TextField(default="old dojo", null=True)

    def __str__(self):
        return f'{self.name} {self.city}'


class ninjas(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dojo = models.ForeignKey(
        Dojo, related_name="ninjas_dojo", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
