from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
	user_id = models.CharField(max_length = 10,primary_key = True)
	name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)

	def __str__(self):
		return self.name.encode('utf-8')

class Item(models.Model):
	item_id = models.AutoField(primary_key=True)
	price = models.IntegerField(null=True)
	description  = models.CharField(max_length=500)
	title = models.CharField(max_length=100)
	status = models.BooleanField(default = False) # status of item
	negotiable = models.BooleanField(default = False) # negotiable or not
	seller = models.ForeignKey(User, null= True, on_delete = models.CASCADE)	
	posted_date = models.DateTimeField(null = True)
	url = models.CharField(max_length=1000,null=True)

class Interest(models.Model):
	interest_id = models.IntegerField(primary_key=True)
	item = models.ForeignKey(Item,null=True, on_delete = models.CASCADE)
	buyer = models.ForeignKey(User,null = True, on_delete = models.CASCADE)
	quoted_price = models.IntegerField(null=True) # price the buyer wants to buy at
	notified_seller = models.BooleanField(default=False)
	