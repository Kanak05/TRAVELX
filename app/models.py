from django.db import models
from django.contrib.auth.models import AbstractBaseUser

#class CustomUser(AbstractBaseUser):
#	username = models.CharField(max_length=255,unique=True)
#	password = models.CharField(max_length=255)

# Create your models here.

class trial(models.Model):
    trial_input_1 = models.CharField(max_length=255,default=None,null=True)
    trial_input_2 = models.IntegerField(default=None,null=True)
    trial_input_3 = models.TimeField(default=None,null=True)

class festival(models.Model):
	fest_name = models.CharField(max_length=255)
	fest_img = models.CharField(max_length=255)
	fest_desc = models.TextField()

	def _str_(self):
		return self.fest_name
	
class package(models.Model):
	city = models.CharField(max_length=255,default=None,blank=True)
	name = models.CharField(max_length=255,default=None,blank=True)
	sub_title = models.CharField(max_length=255,default=None,blank=True)
	img = models.CharField(max_length=255,default=None,blank=True)
	price = models.CharField(max_length=255,default=None,blank=True)
	sub_price = models.CharField(max_length=255,default=None,blank=True)
	discount = models.CharField(max_length=255,default=None,blank=True)
	duration = models.CharField(max_length=255,default=None,blank=True)
	day1 = models.CharField(max_length=255,default=None,blank=True)
	day2 = models.CharField(max_length=255,default=None,blank=True)
	day3 = models.CharField(max_length=255,default=None,blank=True)
	day4 = models.CharField(max_length=255,default=None,blank=True)
	place1 = models.CharField(max_length=255,default=None,blank=True)
	place2 = models.CharField(max_length=255,default=None,blank=True)
	place3 = models.CharField(max_length=255,default=None,blank=True)
	place4 = models.CharField(max_length=255,default=None,blank=True)
	hotel1 = models.CharField(max_length=255,default=None,blank=True)
	hotel2 = models.CharField(max_length=255,default=None,blank=True)
	hotel3 = models.CharField(max_length=255,default=None,blank=True)
	hotel4 = models.CharField(max_length=255,default=None,blank=True)

	def _str_(self):
		return self.name

class client(models.Model):
	username = models.CharField(max_length=255)
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	# photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
	email = models.EmailField(max_length=100)
	password = models.CharField(max_length=50)

	def _str_(self):
		return self.username



class search(models.Model):
	destination = models.CharField(max_length=255)
	link =  models.URLField(default=None, blank=False,null=True)
	Duration = models.CharField(max_length=50)
	details = models.TextField(default=None,blank=True)
	img = models.URLField(default=None, blank=False,null=True)
    # other fields in your model

	def __str__(self):
		return self.destination
	
class payments(models.Model):
	title = models.CharField(max_length=255)
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	budget = models.CharField(max_length=255)
	# photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
	email = models.EmailField(max_length=100)
	phone = models.CharField(max_length=50)
	address = models.TextField()
	month = models.CharField(max_length=50)
	day = models.CharField(max_length=50)
	year = models.CharField(max_length=50)
	departing_from = models.CharField(max_length=50)
	destination = models.CharField(max_length=50)
	no_people = models.CharField(max_length=50)
	
	def _str_(self):
		return self.title