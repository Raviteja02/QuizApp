from django.urls import path
from . import views

urlpatterns = [
	path('', views.AdminPage, name='AdminPage'),
	path('postquestion',views.postquestion,name='postquestion'),
	path('viewquestions',views.viewquestions, name='viewquestions')
]