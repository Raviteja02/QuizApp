from django.contrib.auth.forms import UserCreationForm
from . models import QuizAppUser

class RegistrationForm(UserCreationForm):
	class Meta:
		model = QuizAppUser
		fields= ['username','email','first_name','last_name']