# Generated by Django 3.1.2 on 2020-11-11 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='university',
        ),
    ]
