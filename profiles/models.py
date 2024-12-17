from django.conf import settings
from django.conf.global_settings import LANGUAGES
from django.db import models

# Create your models here.


PLANETS = [
    (0, 'Mercury'),
    (1, 'Venus'),
    (2, 'Earth'),
    (3, 'Mars'),
    (4, 'Jupiter'),
    (5, 'Saturn'),
    (6, 'Uranus'),
    (7, 'Neptune'),
    (8, 'Pluto'),
]

SECURITY_QUESTIONS = (
	(0, 'What was the name of your first pet?'),
	(1, 'What street did you grow up on?'),
	(2, "What is your mother's maiden name?"),
	(3, 'Where was your first date?'),
	(4, 'What is the name of your best childhood friend?'),
)


# Create your models here.
class SpaceTravelerProfile(models.Model):
	REQUIRED_FIELDS = [
		'home_planet',
		'language',
		'security_question',
		'security_answer',
	]
	home_planet = models.IntegerField(
		verbose_name='planet', 
		choices=PLANETS, 
		null=True, blank=False
	)
	age = models.PositiveIntegerField(
		null = True,  # allows the database to store this field as null
		blank = True # allows the user to omit this field when registering
	)
	language = models.CharField(
		max_length=10, 
		choices=LANGUAGES, 
		null=True, blank=True
	)
	bio = models.TextField(
		max_length=200, 
		null=True, blank=True
	)
	security_question = models.IntegerField(
		# max_length=2, 
		choices=SECURITY_QUESTIONS, 
		null=True, blank=False
	)
	security_answer = models.CharField(
		max_length=30, 
		null=True, blank=False
	)

	real_account = models.OneToOneField(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
		related_name='profile',
		null=True, blank=False,
	)

	# def get_profile_is_user(self):
	# 	return self.pk == self.real_account.pk

	def __str__(self) -> str:
		return f"{self.real_account.username}'s profile" #type:ignore
