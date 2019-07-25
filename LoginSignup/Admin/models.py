from django.db import models
from Users.models import QuizAppUser
# Create your models here.

class AdminUser(AbstractUser):
	pass

class Question(models.Model):
	question = models.CharField(max_length=255)

	def __str__(self):
		return self.question

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete= models.CASCADE)
	answer = models.CharField(max_length=50)
	correct  = models.BooleanField(default=False)

	def __str__(self):
		return self.answer

class Guess(models.Model):
	submitted_by = models.ForeignKey(QuizAppUser, on_delete= models.CASCADE)
	answer_given = models.ForeignKey(Choice, on_delete= models.CASCADE)