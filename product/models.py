from django.db import models

# Create your models here.
class ProductModel(models.Model):

	Name = models.CharField(max_length = 50)
	Brand = models.CharField(max_length = 30)
	Color = models.CharField(max_length = 20)
	Image = models.FileField()
	Size = models.IntegerField()
	Price = models.IntegerField()
	Category = models.CharField(max_length=100)
	Details = models.TextField()

	class Meta:
			db_table = 'product'

	def __str__(self):
		    return self.Name

