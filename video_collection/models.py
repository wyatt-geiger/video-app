from django.db import models

# Create your models here.

class Video(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=400)
    notes = models.TextField(blank=True, null=True) # allows null entries in the database

    def __str__(self):
        return f'ID: {self.pk}, Name: {self.name}, URL: {self.url}, Notes: {self.notes[:200]}'
        # truncates notes to first 200 characters
