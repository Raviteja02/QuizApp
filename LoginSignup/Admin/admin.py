from django.contrib import admin
from . models import Question,Choice,Guess

# Register your models here.
class ChoiceAdmin(admin.TabularInline):
	model = Choice
	classes = ('grp-collapse grp-open',)
	extra = 0


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
		inlines = [ChoiceAdmin]
