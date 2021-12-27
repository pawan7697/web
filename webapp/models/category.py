from django.db import models

# Create your models here.

from django.db import models

class category(models.Model):
    cat_name = models.CharField(max_length=100)
    status = models.IntegerField(default=1)

    def __str__(self):

        return self.cat_name

    @staticmethod
    def get_categorty():
        return category.objects.all()    