from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from . forms import RegistrationForm
# Create your views here.

def index(request):
	return render(request, 'index.html')


def usercreation(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
	
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username,password=password)
			login(request,user)
			return redirect('userpage')

	else:
		form = RegistrationForm()
		
	return render(request, 'registration/register2.html',{'form':form})

def userpage(request):
	return render(request,'userpage.html')