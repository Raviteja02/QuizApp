from django.shortcuts import render,redirect
from . models import Question,Choice
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.

def AdminPage(request):
	return render(request, 'AdminPage.html')

def postquestion(request):
	if request.method == 'POST':
		que = request.POST['question']
		option1 = request.POST['option1']
		option2 = request.POST['option2']
		option3 = request.POST['option3']
		option4 = request.POST['option4']
		question = Question.objects.create(question=que)
		try:
			option1_check = request.POST['check_option1']
			choice_1 = Choice.objects.create(question=question, answer=option1, correct=option1_check)
		except:
			choice_1 = Choice.objects.create(question=question, answer=option1)
		try:
			option2_check = request.POST['check_option2']
			choice_2 = Choice.objects.create(question=question, answer=option2, correct=option2_check)
		except:
			choice_2 = Choice.objects.create(question=question, answer=option2)
		try:
			option3_check = request.POST['check_option3']
			choice_3 = Choice.objects.create(question=question, answer=option3, correct=option3_check)
		except:
			choice_3 = Choice.objects.create(question=question, answer=option3)
		try:
			option4_check = request.POST['check_option4']
			choice_3 = Choice.objects.create(question=question, answer=option4, correct=option4_check)
		except:
			choice_3 = Choice.objects.create(question=question, answer=option4)
		
		messages.add_message(request, messages.INFO,'Question Posted Successfully.')
		return redirect('postquestion')
	return render(request,'postquestion.html')


def viewquestions(request):
	questions = Question.objects.all()
	return render(request, 'viewquestions.html',{'questions':questions})



