from django.db import models
from .category import category
# Create your models here.

from django.db import models

class navbar(models.Model):
    menu = models.CharField(max_length=100)
    category = models.ForeignKey(category, default=None,on_delete=models.CASCADE)
    menu_slug = models.SlugField(max_length = 200,default=None)
    status = models.IntegerField(default=1)

    def __str__(self):

        return self.menu
