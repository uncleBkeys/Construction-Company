from distutils.command.upload import upload
from django.db import models


class Applicants(models.Model):
 first_name=models.CharField(max_length=100)
 last_name= models.CharField(max_length=100)
 country= models.CharField(max_length=100)
 nationality= models.CharField(max_length=100)
 phone=models.CharField(max_length=15)
 email=models.EmailField(max_length=45)
 role_of_experience=models.TextField(max_length=120,)

def __str__(self):
    return self.first_name
