# Generated by Django 2.2 on 2020-03-12 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TV_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shows',
            name='desc',
            field=models.TextField(default='prev show', null=True),
        ),
    ]
