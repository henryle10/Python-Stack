# Generated by Django 2.2 on 2020-03-18 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wall_app', '0004_message_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='total_likes',
            field=models.IntegerField(default=0),
        ),
    ]