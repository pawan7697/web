from django.db import models
from .models import navbar

# Create your models here.

from django.db import models

class pages(models.Model):
    page=models.TextField()
    menu = models.ForeignKey(navbar, on_delete=models.CASCADE)
    pic=models.ImageField(upload_to='upload_images/')
    status = models.IntegerField(default=1)
