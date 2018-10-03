from django.db import models

# Create your models here.

class Maintainance(models.Model):
    maintainance_start = models.DateField()
    maintainance_end = models.DateField()
