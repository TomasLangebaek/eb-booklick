# Generated by Django 3.1.1 on 2020-10-15 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('universities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('username', models.CharField(max_length=60, null=True, unique=True)),
                ('password', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='universities.university')),
            ],
        ),
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.user')),
                ('role', models.CharField(max_length=60, null=True)),
            ],
            bases=('users.user',),
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.user')),
                ('materia', models.CharField(max_length=50, null=True)),
            ],
            bases=('users.user',),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.user')),
                ('semester', models.PositiveSmallIntegerField(default=1, null=True)),
                ('major', models.CharField(max_length=60, null=True)),
                ('second_major', models.CharField(max_length=60, null=True)),
            ],
            bases=('users.user',),
        ),
    ]