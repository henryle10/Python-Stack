# Generated by Django 2.2 on 2020-03-10 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninja_app', '0002_dojo_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dojo',
            name='desc',
            field=models.TextField(default='old dojo', null=True),
        ),
    ]