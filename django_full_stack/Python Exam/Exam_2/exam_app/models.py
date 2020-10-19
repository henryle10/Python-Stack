from django.db import models
import re

EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+$")


class UserManager(models.Manager):
    def validator(self, data):
        errors = {}
        if len(data["fname"]) < 2:
            errors["fname"] = "First name has to be 2 chars"
        if len(data["lname"]) < 2:
            errors["lname"] = "Last name has to be 2 chars"
        if not EMAIL_REGEX.match(data["email"]):
            errors["email"] = "Email is invalid"
        if data["password"] != data["cpassword"]:
            errors["password"] = "Passwords do not match"
        if len(data["password"]) < 8:
            errors["password"] = "Password is too short"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


class WishManager(models.Manager):
    def validator(self, data):
        errors = {}
        if len(data["wish"]) < 3:
            errors["wish"] = "A wish must consist of a least 3 characters!"
        if len(data["desc"]) < 1:
            errors["desc"] = "a description must be provided!"
        return errors


class Wish(models.Model):
    item = models.CharField(max_length=255)
    description = models.TextField()
    like = models.ManyToManyField(User, related_name="user_likes")
    total_likes = models.IntegerField(default=0)
    wished_by = models.ForeignKey(
        User, related_name="User_wishes", on_delete=models.CASCADE
    )
    grant_wish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = WishManager()
