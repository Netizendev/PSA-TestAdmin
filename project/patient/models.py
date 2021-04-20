from django.db import models

# Create your models here.

class Patient(models.Model):
	name = models.CharField(max_length=150)
	ssn = models.CharField(max_length=100)