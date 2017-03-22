from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'offers',views.display_my_offers,name = 'offers'),
    url(r'bids', views.display_bids , name = 'bids'),
    url(r'createoffer',views.create_offer, name= 'create_offer'),
    url(r'closeoffer',views.close_offer, name = 'close_offer'),
    url(r'sendinterest',views.send_interest,name = 'send_interest'),
    url(r'cancelinterest', views.cancel_interest, name = 'cancel_interest'),
    url(r'interests',views.get_all_interests, name = 'get_all_interests'),
    url(r'createuser',views.create_user, name = 'create_user'),
    ]