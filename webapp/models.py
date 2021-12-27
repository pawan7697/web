from django.db import models

# Create your models here.

from django.db import models

class navbar(models.Model):
    menu = models.CharField(max_length=100)
    status = models.IntegerField(default=1)
