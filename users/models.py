from django.db import models
from universities.models import University
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    #Creo que falta crear herencia a usuario default de django
    name = models.CharField(
        max_length = 50,
        null = True
    )
    last_name = models.CharField(
        max_length = 50,
        null = True
    )
    username = models.CharField(
        max_length = 60,
        null = True,
        unique = True
    )
    password = models.CharField(
        max_length = 50,
        null = True,
        blank = True
    )
    email = models.EmailField(
        null = True
    )
    edad = models.PositiveSmallIntegerField(
        default = 10
    )
    genero = models.CharField(
        max_length = 60,
        null = True,
        unique = True
    )
    codigo = models.CharField(
        max_length = 60,
        null = True,
        unique = True
    )
    
    def __str__(self):
        return str(self.username) + ' w/ id: ' + str(id)

class Professor(Users):
    materia = models.CharField(
        max_length = 50,
        null = True
    )
    
class Student(Users):
    semester = models.PositiveSmallIntegerField(
        default = 1,
        null = True
    )
    major = models.CharField(
        max_length = 60,
        null = True
    )
    second_major = models.CharField(
        max_length = 60,
        null = True
    )

class Administrator(Users):
    role = models.CharField(
        max_length = 60,
        null = True
    )