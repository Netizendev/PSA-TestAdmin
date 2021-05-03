from django.db import models
from django.urls import reverse

from datetime import datetime, timedelta

# Create your models here.

class Provsvar(models.Model):
	created = models.DateField(auto_now_add=True)
	ssn = models.CharField(max_length=100)
	result = models.DecimalField(max_digits=5, decimal_places=2)
	
	def __str__(self):
		return self.ssn

class Patient(models.Model):
	ssn = models.CharField(max_length=100, primary_key=True, unique=True)
	namn = models.CharField(max_length=150, default='Okänd')
	gata = models.CharField(max_length=150, default='Okänd')
	postort = models.CharField(max_length=150, default='Okänd')
	postnr = models.CharField(max_length=150, default='Okänd')
	mail = models.CharField(max_length=150, default='Okänd')
	operationsdatum = models.DateField()
	created = models.DateField(auto_now_add=True)
	kallelsedatum = models.DateField()

	def save(self, *args, **kwargs):
		self.kallelsedatum = self.operationsdatum + timedelta(days=180)
		super().save(*args, **kwargs)  # Call the "real" save() method.
        
		
	# def uppdate_kallesledatum(self,):
	# 	self.kallelsedatum = self.kallelsedatum + timedelta(days = 180)

	def __str__(self):
		return self.namn

class Kallelse(models.Model):
	ssn = models.CharField(max_length=100)
	name = models.CharField(max_length=150, default='Okänd')
	datum = models.DateField()
	
	def __str__(self):
		return self.ssn