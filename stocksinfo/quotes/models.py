from django.db import models

# Create your models here.

class stocks(models.Model):
	"""docstring for stocks"""
	ticker =models.CharField(max_length=12)
	
	def __str__(self):
		return self.ticker
		