from django.forms import ModelForm

from .models import SpaceTravelerProfile


class SpaceTravelerProfileForm(ModelForm):
	class Meta:
		model = SpaceTravelerProfile
		fields = [
			'home_planet', 
			'language', 
			'age', 
			'bio', 
			'security_question', 
			'security_answer',
			'real_account',
		]
		exclude = ['real_account']
