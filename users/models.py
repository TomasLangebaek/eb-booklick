from django.db import models

class User(models.Model): #Creo que falta crear herencia a usuario default de django
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
    university = models.ForeignKey( University,
        on_delete = models.CASCADE
    )
    #Falta agregar relación a universidad: university: FK ?
    #Falta agregar relación a contenido: content, FK ?
    #Falta agregar relación a los tags: tags, ManyToMany
    
    def __str__(self):
        return self.username + ' w/ id: ' + id

class Professor(User):
    materia = models.CharField(
        max_length = 50,
        null = True
    )
    
class Student(User):
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

class Administrator(User):
    role = models.CharField(
        max_length = 60,
        null = True
    )