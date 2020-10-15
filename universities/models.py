from django.db import models

class University(models.Model):
    name = models.CharField(
        max_length = 50,
        null = False
    )
    location = models.CharField(
        max_length = 90,
        null = False
    )
    def __str__(self):
        return self.name + ' w/ id: ' +  id