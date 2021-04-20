# Create your models here.

class Patients(models.Model):
	name = models.CharField(max_length=200)
    ssn = models.CharField(max_length=200)
    frequency = models.CharField(max_length=200)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.ssn
