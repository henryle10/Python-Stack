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


class MsgManager(models.Manager):
    def validator(self, data):
        errors = {}
        if len(data["message"]) < 1:
            errors["message"] = "message must be longer than 1 char"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


class Message(models.Model):
    message = models.TextField()
    user = models.ForeignKey(
        User, related_name="user_messages", on_delete=models.CASCADE
    )
    like = models.ManyToManyField(User, related_name="User_likes")
    total_likes = models.IntegerField(0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MsgManager()


class Comment(models.Model):
    comment = models.TextField()
    message = models.ForeignKey(
        Message, related_name="msg_comments", on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User, related_name="user_comments", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
