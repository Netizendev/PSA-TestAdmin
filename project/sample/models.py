from django.db import models

class Sample(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    ssn = models.CharField(max_length=100)
    result = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return self.ssn