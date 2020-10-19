from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+$')


class UserManager(models.Manager):
    def validator(self, data):
        errors = {}
        if len(data['fname']) < 2:
            errors['fname'] = "First name has to be 2 chars"
        if len(data['lname']) < 2:
            errors['lname'] = "Last name has to be 2 chars"
        if not EMAIL_REGEX.match(data['email']):
            errors['email'] = "Email is invalid"
        if data['password'] != data['cpassword']:
            errors['password'] = "Passwords do not match"
        if len(data['password']) < 8:
            errors['password'] = "Password is too short"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # an instance of our manager so we can access the validations function
    objects = UserManager()
