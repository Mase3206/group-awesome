from django.test import TestCase
from django.urls import reverse
from .apps import get_all_profiles
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

# Create your tests here.


class NewSignUpTests(TestCase):
	def test_newUsersRedirectedToCreate(self):
		response = self.client.post(
			reverse('account_signup'),
			{
				'username': 'testuser',
				'email': 'testuser@example.com',
				'password1': 'testpass123',
				'password2': 'testpass123',
			}
		)
		self.assertEqual(response.status_code, 302)
		self.assertRedirects(response, '/profiles/create/')



class NewProfileTests(TestCase):
	def setUp(self):
		self.signupResponse = self.client.post(
			reverse('account_signup'),
			{
				'username': 'testuser',
				'email': 'testuser@example.com',
				'password1': 'testpass123',
				'password2': 'testpass123',
			}
		)

		self.client.login(username='testuser', password='testpass123')
		self.shouldBe_profileData = {
			'home_planet': 2,
			'age': 31,
			'language': 'en',
			'bio': 'am duck',
			'security_question': 0,
			'security_answer': 'Bob',
		}


	def test_profileCreation(self):
		eq = self.assertEqual

		allUserObjects = get_user_model().objects.all()
		eq(allUserObjects.count(), 1)  # make sure only one user was created
		eq(allUserObjects[0].username, 'testuser')

		response = self.client.post(
			reverse('profiles:create'),
			self.shouldBe_profileData
		)

		eq(response.status_code, 302)

		allProfileObjects = get_all_profiles().objects.all()
		eq(allProfileObjects.count(), 1)
		# owned by that user
		eq(allProfileObjects[0].real_account.pk, 1) #type:ignore
		
		# all data was set correctly
		for k in self.shouldBe_profileData.keys():
			eq(
				getattr(allProfileObjects[0], k),
				self.shouldBe_profileData[k]
			)
		

	def test_profileChange(self):
		eq = self.assertEqual

		create = self.client.post(
			reverse('profiles:create'),
			self.shouldBe_profileData
		)


		changeData = self.shouldBe_profileData
		changeData['bio'] = 'am human now'
		response = self.client.post(
			reverse('profiles:update', kwargs={'pk': 1}),
			changeData
		)

		eq(response.status_code, 302)

		allProfileObjects = get_all_profiles().objects.all()
		eq(allProfileObjects.count(), 1)
		# owned by that user
		eq(allProfileObjects[0].real_account.pk, 1) #type:ignore
		
		# all data was set correctly
		for k in changeData.keys():
			eq(
				getattr(allProfileObjects[0], k),
				changeData[k]
			)
