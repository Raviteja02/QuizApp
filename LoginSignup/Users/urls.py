from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('register', views.usercreation, name='register'),
	path('userpage', views.userpage, name='userpage')
]