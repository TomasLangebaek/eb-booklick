from django.db import models

class Tag(models.Model):
    name = models.CharField(
        max_length = 80,
        null = False
    )

    def __str__(self):
        return self.name + ' w/ id: ' + id
