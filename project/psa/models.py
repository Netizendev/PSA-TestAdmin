from django.db import models

# Create your models here.

class Provsvar(models.Model):
	created = models.DateField(auto_now_add=True)
	ssn = models.CharField(max_length=100)
	result = models.DecimalField(max_digits=5, decimal_places=2)
	
	def __str__(self):
		return self.created, self.ssn
	def get_absolute_url(self):
		return reverse('add_provsvar', kwargs={'pk': self.pk})

class Patient(models.Model):
	ssn = models.CharField(max_length=100, primary_key=True, unique=True)
	namn = models.CharField(max_length=150, default='Okänd')
	gata = models.CharField(max_length=150, default='Okänd')
	postort = models.CharField(max_length=150, default='Okänd')
	postnr = models.CharField(max_length=150, default='Okänd')
	mail = models.CharField(max_length=150, default='Okänd')
	opdate = models.DateField(auto_now_add=True)
	created = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.namn

class Kallelse(models.Model):
	ssn = models.CharField(max_length=100)
	name = models.CharField(max_length=150, default='Okänd')
	datum = models.DateField()
	
	def __str__(self):
		return self.ssn