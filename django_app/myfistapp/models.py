from __future__ import unicode_literals
from django.db import models
from decimal import Decimal
# Create your models here.

class EmpName(models.Model):
    name=models.CharField(max_length=200)

class EMpProfile(models.Model):
    name=models.CharField(max_length=200)
    salary=models.DecimalField(max_digits=6,decimal_places=4,default=Decimal('0.00000'))


