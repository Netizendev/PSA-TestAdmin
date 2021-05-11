from django.db import models
from django.urls import reverse
import sqlite3

from datetime import datetime, timedelta
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Create your models here.

def read_from_db(value):
	x = str(value)
	con = sqlite3.connect('db.sqlite3')
	cur = con.cursor()
	cur.execute("SELECT 1 FROM psa_patient where ssn = ?", (x,))
	y = cur.fetchall()
	if y:
		pass
	else:
		raise ValidationError(_('%(value)s personnummer saknas i databasen'), params={'value': value},)


def validate_ssn(value):
	x = str(value)
	if len(x) is not 10:
		raise ValidationError(_('%(value)s är inte ett giltigt personnummer. Ange tio siffror utan sträck..'), params={'value': value},)

def validate_postnr(value):
	if value <= 10000 or value >= 99999:
		raise ValidationError(_('%(value)s är inte en giltig postkod. Ange en giltig postkod 5 siffror utan mellanrum.'), params={'value': value},)

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
	
	class Meta:
		verbose_name_plural = "Patienter"

	def __str__(self):
		return self.namn

	def save(self, *args, **kwargs):
		self.kallelsedatum = self.operationsdatum + timedelta(days=180)
		super().save(*args, **kwargs)  # Call the "real" save() method.

class Provsvar(models.Model):
	created = models.DateField(auto_now_add=True)
	result = models.DecimalField(max_digits=5, decimal_places=2)
	done = models.CharField(max_length=100, default='False')
	ssn = models.ForeignKey(Patient, default='None', verbose_name="Kopplad patient", on_delete=models.SET_DEFAULT, validators=[validate_ssn, read_from_db])
	
	def __str__(self):
		return str(self.created)
	
	class Meta:
		verbose_name_plural = "Provsvar"

class Hantera(models.Model):
	ssn = models.CharField(max_length=100, primary_key=True)
	name = models.CharField(max_length=150)
	result = models.CharField(max_length=150)

	def __str__(self):
		return self.ssn