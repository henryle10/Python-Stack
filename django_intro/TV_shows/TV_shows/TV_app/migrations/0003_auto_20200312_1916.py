# Generated by Django 2.2 on 2020-03-13 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TV_app', '0002_shows_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shows',
            name='desc',
            field=models.TextField(null=True),
        ),
    ]
