from django.db import models
from django.urls import reverse

from datetime import datetime, timedelta
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Create your models here.

def validate_ssn(value):
	x = str(value)
	if len(x) is not 10:
		raise ValidationError(_('%(value)s is not a valid social security number. Please enter av valid ssn containing ten numbers without a hyphen.'), params={'value': value},)

def validate_postnr(value):
	if value <= 10000 or value >= 99999:
		raise ValidationError(_('%(value)s is not a valid postal code. Please enter a valid postal code containing five numbers only.'), params={'value': value},)

class Provsvar(models.Model):
	created = models.DateField(auto_now_add=True)
	ssn = models.BigIntegerField(validators=[validate_ssn])
	result = models.DecimalField(max_digits=5, decimal_places=2)
	done = models.CharField(max_length=100, default='False')
	
	def __str__(self):
		return self.ssn

class Patient(models.Model):
	ssn = models.BigIntegerField(validators=[validate_ssn],primary_key=True, unique=True)
	namn = models.CharField(max_length=100)
	gata = models.CharField(max_length=50)
	postort = models.CharField(max_length=50)
	postnr = models.IntegerField(validators=[validate_postnr])
	mail = models.EmailField(max_length=50)
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