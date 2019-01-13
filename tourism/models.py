from django.db import models

# Create your models here.

class HillStations(models.Model):
	"""Name,Region,Type,airport_dist(km),
	railway_dist(km),Elevation(m),avg_rating"""

	name = models.CharField(max_length=300)
	region = models.CharField(max_length=300)
	airport_dist = models.FloatField()
	railway_dist = models.FloatField()
	elevation = models.IntegerField()
	avg_rating = models.FloatField()
	logo = models.FileField()

	def __str__(self):

		return self.name



