from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


class HomepageTests(TestCase):
	def test_homepageViewExistsAtCorrectUrl(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)
	
	def test_signupViewName(self):
		response = self.client.get(reverse('home'))

		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'home.html')
