from django.db import models

class  Segment(models.Model):
	time = models.FloatField(max_length = 100)
	log = models.FloatField(max_length = 100)
	lat = models.FloatField(max_length = 100)
	breath = models.FloatField(max_length = 100)
	def __unicode__(self):
		return str(self.time)
	
class Trip(models.Model):
	name = models.CharField(max_length = 100)
	date = models.DateField()
	recording = models.ManyToManyField(Segment)	
	def __unicode__(self):
		return self.name
