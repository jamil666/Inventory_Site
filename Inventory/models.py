from django.db import models


# Create your models here.

class Computer(models.Model):

    hostname = models.CharField(max_length=100, null=True, unique=True)
    description = models.CharField(max_length=200, null=True)
    model = models.CharField(max_length=100, null=True)
    serial = models.CharField(max_length=100, null=True, unique=True)
    date = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.hostname

