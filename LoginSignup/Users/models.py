from django.db import models
from django.contrib.auth.models import AbstractUser
import pytz
from timezone_field import TimeZoneField


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None, null=True)
    question = models.CharField(max_length=255)

    def __str__(self):
        return self.question


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=50)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer


class QuizAppUser(AbstractUser):
    pass


class Quiz(models.Model):
    owner = models.ForeignKey(QuizAppUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    score = models.CharField(max_length=10, null=True)


class Guess(models.Model):
    submitted_by = models.ForeignKey(QuizAppUser, on_delete=models.CASCADE)
    answered_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_given = models.ForeignKey(Choice, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)


class Producer(models.Model):
    queue = models.CharField(max_length=50)
    exchange = models.CharField(max_length=50)
    routing_key = models.CharField(max_length=50,blank=True,null=True)
    body = models.CharField(max_length=1000,blank=True,null=True)