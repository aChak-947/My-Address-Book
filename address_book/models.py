from django.db import models

# Create your models here.
class Address(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField(max_length=200)
	phone = models.CharField(max_length=15)
	address = models.CharField(max_length=200)
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	phone = models.CharField(max_length=10)

	def _str_(self):
		return self.name