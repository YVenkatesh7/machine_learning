from django.db import models

# Create your models here.
class Employee(models.Model):
	eid = models.IntegerField()
	name = models.CharField(max_length=100)
	email = models.EmailField()
	address = models.CharField(max_length=200)
	contact = models.IntegerField()
	class Meta:
		db_table = "employee"
