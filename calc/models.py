from django.db import models

# Create your models here.
class CalcModel(Models.model):
	name = models.CharField(max_length=50)
	email = models.EmailField()
	mobile = models.BigIntegerField()
	salary = models.IntegerField()
	address = models.TextField()
	class meta:
		db_table = 'demo'
