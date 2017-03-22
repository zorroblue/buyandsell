from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import *
from .models import *
import json
from django.core import serializers
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response,render,get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
# Create your views here.

# Create a new user for the DB here
@csrf_exempt
def create_user(request):
	if request.method == 'POST':
		try:
			userid = request.POST.get('userid')
			name = request.POST.get('name')
			contact = request.POST.get('contact')
			print "User",userid
			user = User.objects.filter(user_id__exact = userid)
			print user
			# if user already exists
			print len(user)
			if len(user)!=0:
				return JsonResponse({'status':'exists'})
			
			user = User(user_id = userid, name = name, contact = contact)
			user.save()
			return JsonResponse({'status':'success'})
		except:
			return JsonResponse({'status' : 'failure'})

#Create a new offer
#POST
# params {price, description, title, sellerid}
@csrf_exempt
def create_offer(request):
	if request.method == 'POST':
		try:
			price = request.POST.get('price')
			description  = request.POST.get('description')
			title = request.POST.get('title')
			status = False # status of item
			negotiable = True # negotiable or not
			sellerid = request.POST.get('sellerid')
			seller = User.objects.get(user_id= sellerid)	
			print seller
			posted_date = timezone.now()
			offer = Item(price = price , description = description, posted_date = posted_date, status = status , title = title, negotiable = negotiable, seller = seller)
			offer.save()
			return JsonResponse({'status':'success'})
		except:
			return JsonResponse({'status' : 'failure'})

# Display all my offers
#GET
#params {userid}
@csrf_exempt
def display_my_offers(request):
	if request.method == 'GET':
		userid = request.GET.get('userid')
		#bids = Item.objects.all()
		print userid
		bids = Item.objects.filter(seller__user_id__exact = userid)
		return JsonResponse(json.loads(serializers.serialize('json',bids)),safe = False)

#Display bids which are available and are not mine
#params {userid}
#GET
def display_bids(request):
	# don't show my bids
	if request.method == 'GET':
		pk = request.GET.get('userid')
		print pk
		bids = Item.objects.filter(status__exact = False).exclude(seller__user_id__exact = pk)
		return JsonResponse(json.loads(serializers.serialize('json',bids)),safe=False)

#update/close the offer
#params {userid, itemid}
#POST
@csrf_exempt
def close_offer(request):

	print request.method
	if request.method == 'POST':
		userid = request.POST.get('userid')
		itemid = request.POST.get('itemid')
		
		print userid,itemid
		try:
			item = Item.objects.get(item_id = itemid)
			#print item.seller.user_id,userid
			if item.seller.user_id == userid:
				#Item.objects.filter(item_id__exact = itemid).update(status__exact = True)
				Item.objects.filter(item_id__exact = itemid).delete()
				return JsonResponse({'status':'success'})
			else:
				return JsonResponse({'status':'success'})
		except Exception as e :
			#print str(e)
			return JsonResponse({'status' : 'failure'})


 #select the bid to buy
 #params {userid, itemid}
@csrf_exempt
def send_interest(request):
 	if request.method == 'POST':
 		userid = request.POST.get('userid')
 		itemid = request.POST.get('itemid')
 		print userid,itemid
 		#while True:
 		try:
 			user = User.objects.get(user_id = userid)
 			item = Item.objects.get(item_id = itemid )
 			interest = Interest(buyer = user, item = item )
 			interest.save()
 			return JsonResponse({'status' : 'success'})
 		except:
 			return JsonResponse({'status':'failure'})	

# cancel interest
#params {userid, itemid}
@csrf_exempt
def cancel_interest(request):
	if request.method == 'POST':
 		interestid = request.POST.get('interestid')
 		try:
 			interest = Interest.objects.filter(interest_id__exact = interestid).delete()
 			print interest
 			return JsonResponse({'status' : 'success'})
 		except:
 			return JsonResponse({'status':'failure'})	

# get all interest messages for bids by user
# params {userid}
@csrf_exempt
def get_all_interests(request):
	if request.method == 'GET':
		userid = request.GET.get('userid')
		interests = Interest.objects.filter(item__seller__user_id = userid)
		#interests = Interest.objects.all()
		return JsonResponse(json.loads(serializers.serialize('json',interests)),safe=False)