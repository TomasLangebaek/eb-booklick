from django.db import models
from users.models import User

class Booklist(models.Model):
    name = models.CharField(
        max_length = 50,
        null = False
    )
    description = models.TextField(
        blank = True,
        null = True
    )
    users = models.ManyToManyField(User)
    #Falta agregar comentarios y likes, pero creo que deberían ser clases aparte
    def __str__(self):
        return self.name + ' w/ id: ' + id
