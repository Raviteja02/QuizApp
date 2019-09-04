from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('register', views.usercreation, name='register'),
	path('accounts/login/', views.userpage, name='userpage'),
	path('accounts/login/userpage/', views.userauthentication, name='userauthentication'),
	path('postcategory',views.postcategory,name='postcategory'),
	path('postquestion',views.postquestion,name='postquestion'),
	path('viewquestions',views.viewquestions, name='viewquestions'),
	path('editquestion/<int:pk>/', views.editquestions, name='editquestion'),
	path('viewhistory', views.viewhistory, name='viewhistory'),
	path('takequiz/<int:pk>/',views.takequiz, name='takequiz'),
	path('result/<int:pk>/', views.result, name='result'),
	path('success',views.success, name='success'),
	path('questionlist', views.QuestionList.as_view(), name='questionlist'),
	path('questiondetal/<int:pk>/',views.QuestionDetail.as_view(),name='questiondetail'),
    path('questionslist/',views.QuestionsList.as_view(),name='questionslist'),
	path('producer/',views.Producers.as_view(),name='prodcer')
]