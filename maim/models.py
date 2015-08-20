from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class WebUser(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	profile_picture = models.ImageField(upload_to="Travel", null=True)
	bio = models.TextField()
	# picture = models.ForeignKey('maim.Picture', null=True)

	def __unicode__(self):
		return self.first_name




class Picture(models.Model):
	image = models.ImageField(upload_to="Travel")
	country = models.CharField(max_length=50)
	city = models.CharField(max_length=50)
	comment = models.ForeignKey('maim.Comments', null=True, blank=True)

	def __unicode__(self):
		return self.country




class Comments(models.Model):
	comment = models.TextField()
	reply = models.ForeignKey('maim.Comments', null=True, blank=True)

	def __unicode__(self):
		return self.Picture.comment
