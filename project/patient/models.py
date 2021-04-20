from django.db import models

# Create your models here.

class Patient(models.Model):
	ssn = models.CharField(max_length=100, primary_key=True, unique=True)
	frekvens = models.CharField(max_length=150, default='Okänd')
	name = models.CharField(max_length=150, default='Okänd')
	gata = models.CharField(max_length=150, default='Okänd')
	postort = models.CharField(max_length=150, default='Okänd')
	telefon = models.CharField(max_length=150, default='Okänd')
	mail = models.CharField(max_length=150, default='Okänd')
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name