# Generated by Django 3.1.2 on 2020-12-14 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_users_edad'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='genero',
            field=models.CharField(max_length=60, null=True, unique=True),
        ),
    ]
