from django.contrib import admin
from django.db import models
from django.db.models.base import Model

from .models.models import navbar
from .models.pages import pages
from .models.category import category
from .models.enquiry import enquiry

class Adminnavbar(admin.ModelAdmin):
    list_display=['menu','category','status']

class Adminpages(admin.ModelAdmin):
    list_display=['page', 'menu','pic','status']

class Admincategory(admin.ModelAdmin):
    list_display=['cat_name','status']     
class Adminenquiry(admin.ModelAdmin):
    list_display=['name','subject','email','phone','mssage','status'] 

admin.site.register(navbar,Adminnavbar)
admin.site.register(pages,Adminpages)
admin.site.register(category,Admincategory)
admin.site.register(enquiry,Adminenquiry)


# Register your models here.
