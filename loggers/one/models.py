from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(verbose_name="Название", max_length=255)

    def __str__(self):
        return self.name