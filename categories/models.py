from django.db import models
# Create your models here.

class CategoriesModel(models.Model):
	cat_name = models.CharField(max_length = 100)

	class Meta:
			db_table = 'categories'

	def __str__(self):
			return self.cat_name