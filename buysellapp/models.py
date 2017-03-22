from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
	user_id = models.CharField(max_length = 10,primary_key = True)
	name = models.CharField(max_length=100)
	contact = models.IntegerField()

	def __str__(self):
		return self.name.encode('utf-8')

class Item(models.Model):
	item_id = models.IntegerField(primary_key=True)
	price = models.IntegerField(null=True)
	description  = models.CharField(max_length=500)
	title = models.CharField(max_length=100)
	status = models.BooleanField(default = False) # status of item
	negotiable = models.BooleanField(default = True) # negotiable or not
	seller = models.ForeignKey(User, null= True, on_delete = models.CASCADE)	
	posted_date = models.DateTimeField(null = True)

class Interest(models.Model):
	interest_id = models.IntegerField(primary_key=True)
	item = models.ForeignKey(Item,null=True)
	buyer = models.ForeignKey(User,null = True)
