from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import RegistrationForm
from . models import QuizAppUser
# Register your models here.


class CustomUserAdmin(UserAdmin):
	add_form = RegistrationForm
	model = QuizAppUser
	list_display = ['username','email','first_name','last_name']

admin.site.register(QuizAppUser,CustomUserAdmin)