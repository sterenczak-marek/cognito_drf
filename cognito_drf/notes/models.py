from django.db import models


class Note(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text
