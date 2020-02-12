from django.db import models

# Create your models here.
class school(models.Model):
	fname = models.CharField(max_length=30)
	lname = models.CharField(max_length=30)
	email = models.EmailField()
	dob = models.DateField()
