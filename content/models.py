from django.db import models

class Content(models.Model):
    title = models.CharField(
        max_length = 50,
        null = True
    )
    description = models.TextField(
        blank = True,
        null = True,
    )
    #Falta agregar asociación a usuario: author FK?
    #Falta agregar relación a tags: tags, ManyToMany?
    def __str__(self):
        return self.title + ' by author: ' + self.author + ' w/ id: ' + id
