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

    def get_absolute_url(self):
        return reverse("basic_app:addsuccess")


