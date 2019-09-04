from django import template

register = template.Library()

	
@register.filter
	def in_question(choices,question):
		return choices.filter(question=question)