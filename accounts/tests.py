from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import UserProfile

class AccountsTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_register(self):
        response = self.client.post(
            reverse('register'),
            {
                'username': 'testuser',
                'email': 'test@example.com',
                'password1': 'testpass123',
                'password2': 'testpass123',
                'phone_number': '1234567890',
                'address': 'Test Address'
            }
        )
        self.assertEqual(response.status_code, 302)  # Redirect after success
        
        # Verify user was created
        user = User.objects.get(username='testuser')
        self.assertEqual(user.email, 'test@example.com')
        
        # Verify profile was created
        profile = UserProfile.objects.get(user=user)
        self.assertEqual(profile.phone_number, '1234567890')
        self.assertEqual(profile.address, 'Test Address')

    def test_login(self):
        # Create a test user
        User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        
        response = self.client.post(
            reverse('login'),
            {
                'username': 'testuser',
                'password': 'testpass123'
            }
        )
        self.assertEqual(response.status_code, 302)  # Redirect after success

    def test_profile_update(self):
        # Create a test user and log in
        user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        UserProfile.objects.create(
            user=user,
            phone_number='1234567890',
            address='Old Address'
        )
        self.client.login(username='testuser', password='testpass123')
        
        # Update profile
        response = self.client.post(
            reverse('profile'),
            {
                'phone_number': '9876543210',
                'address': 'New Address'
            }
        )
        self.assertEqual(response.status_code, 302)  # Redirect after success
        
        # Verify profile was updated
        profile = UserProfile.objects.get(user=user)
        self.assertEqual(profile.phone_number, '9876543210')
        self.assertEqual(profile.address, 'New Address')

    def test_logout(self):
        # Create a test user and log in
        User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.login(username='testuser', password='testpass123')
        
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Redirect after success
