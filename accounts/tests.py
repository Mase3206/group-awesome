from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse




class ManualUserCreationTests(TestCase):
	"""
	Manually verifies that regular users and superusers are created successfully and with the correct fields set.
	"""

	def test_createRegularUser(self):
		eq = self.assertEqual

		User: SpaceTraveler = get_user_model() #type:ignore
		user = User.objects.create_user(
			username='testuser',
			email='testuser@example.com',
			password='testpass1234',
		)

		eq(user.username, 'testuser')
		eq(user.email, 'testuser@example.com')

		self.assertTrue(user.is_active)
		# make sure they're not a god
		self.assertFalse(user.is_staff)
		self.assertFalse(user.is_superuser)


	def test_createSuperuser(self):
		eq = self.assertEqual

		User: SpaceTraveler = get_user_model() #type:ignore
		superuser = User.objects.create_superuser(
			username='testsuperuser',
			email='testsuperuser@example.com',
			password='testpass1234',
		)

		eq(superuser.username, 'testsuperuser')
		eq(superuser.email, 'testsuperuser@example.com')
		
		self.assertTrue(superuser.is_active)
		# make sure they ARE a god
		self.assertTrue(superuser.is_staff)
		self.assertTrue(superuser.is_superuser)

		


class SignUpFormTests(TestCase):
	"""
	Verify the functionality of the signup form.
	"""

	def test_signupViewExistsAtCorrectUrl(self):
		"""Tests the location of the sign-up form view, verifying that it is at the expected location."""
		response = self.client.get('/accounts/signup/')

		self.assertEqual(response.status_code, 200)


	def test_signupViewName(self):
		response = self.client.get(reverse('account_signup'))

		self.assertEqual(response.status_code, 200)


	def test_signupForm(self):
		response = self.client.post(
			reverse('account_signup'),
			{
				'username': 'testuser',
				'email': 'testuser@example.com',
				'password1': 'testpass123',
				'password2': 'testpass123',
			}
		)

		self.assertEqual(response.status_code, 302)  # this should send you home if successful

		allUserObjects = get_user_model().objects.all()
		self.assertEqual(allUserObjects.count(), 1)  # make sure only one user was created
		self.assertEqual(allUserObjects[0].username, 'testuser')
		self.assertEqual(allUserObjects[0].email, 'testuser@example.com')



class UserEditFormTests(TestCase):
	"""
	Verify the functionality of the user modify form
	"""

	def test_modifyViewExistsAtCorrectUrlAndRedirects(self):
		response = self.client.get('/accounts/1/update/')

		self.assertEqual(response.status_code, 302) # should redirect, because we're not signed in

	def test_modifyViewName(self):
		response = self.client.get(reverse('accounts_info_update', kwargs={'pk': 1}))

		self.assertEqual(response.status_code, 302) # should redirect, because we're not signed in

	def test_modifyForm(self):
		# sign up
		signup = self.client.post(
			reverse('account_signup'),
			{
				'username': 'testuser',
				'email': 'testuser@example.com',
				'password1': 'testpass123',
				'password2': 'testpass123',
			}
		)
		self.assertRedirects(signup, '/profiles/create/')

		self.client.login(username='testuser', password='testpass123')
		response = self.client.post(
			reverse('accounts_info_update', kwargs={'pk': 1}),
			{
				'email': 'newemail@example.com',
				'first_name': 'Test',
				'last_name': 'User',
			}
		)

		self.assertEqual(response.status_code, 302)

		allUserObjects = get_user_model().objects.all()
		self.assertEqual(allUserObjects.count(), 1)  # make sure only one user was created
		self.assertEqual(allUserObjects[0].email, 'newemail@example.com')
		self.assertEqual(allUserObjects[0].first_name, 'Test')
		self.assertEqual(allUserObjects[0].last_name, 'User')