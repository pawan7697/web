from django.db import models

# Create your models here.

from django.db import models

class enquiry(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    mssage = models.TextField()
    status = models.IntegerField(default=1)
