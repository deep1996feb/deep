from django.db import models

# Create your models here.
class SliderModel(models.Model):
	name = models.CharField(max_length=50);
	image = models.FileField();

	class Meta:
			db_table = 'Slider'

	def __str__(self):
		    return self.name
