from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

def __str__(self):
	return self.user.username


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=256)
    ceoname = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    

    def __str__(self):
        return self.name



class Employee(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    company = models.ForeignKey(Company,on_delete=models.PROTECT,related_name='employees')

    def __str__(self):
        return self.name
