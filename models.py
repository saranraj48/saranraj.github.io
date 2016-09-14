from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Person(models.Model): 
    id = models.AutoField(primary_key=True)
    mailid = models.CharField(max_length=30, unique=True)
    candidate = models.CharField(max_length=50)
    college = models.CharField(max_length=150)
    accomodation = models.CharField(max_length=10, default="other")
    department = models.CharField(max_length=10, default="No")
    workshop1 = models.CharField(max_length=10, default="None")
    workshop2 = models.CharField(max_length=10, default="None")
    payment = models.CharField(max_length=10, default="Not Paid")
    phone = models.CharField(max_length=10, default="0000000000")
