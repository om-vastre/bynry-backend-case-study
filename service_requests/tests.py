from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import ServiceRequest

class ServiceRequestTests(TestCase):
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        # Create test client
        self.client = Client()
        self.client.login(username='testuser', password='testpass123')

    def test_create_request(self):
        response = self.client.post(
            reverse('create_request'),
            {
                'title': 'Test Request',
                'description': 'Test Description',
            }
        )
        self.assertEqual(response.status_code, 302)  # Redirect after success
        
        # Verify request was created
        request = ServiceRequest.objects.get(title='Test Request')
        self.assertEqual(request.user, self.user)
        self.assertEqual(request.status, 'pending')

    def test_request_list(self):
        # Create a test request
        ServiceRequest.objects.create(
            user=self.user,
            title='Test Request',
            description='Test Description'
        )
        
        response = self.client.get(reverse('request_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'service_requests/request_list.html')
        self.assertContains(response, 'Test Request')

    def test_request_detail(self):
        # Create a test request
        request = ServiceRequest.objects.create(
            user=self.user,
            title='Test Request',
            description='Test Description'
        )
        
        response = self.client.get(reverse('request_detail', args=[request.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'service_requests/request_detail.html')
        self.assertContains(response, 'Test Request')

    def test_update_request_status(self):
        # Create a test request
        request = ServiceRequest.objects.create(
            user=self.user,
            title='Test Request',
            description='Test Description'
        )
        
        response = self.client.post(
            reverse('request_detail', args=[request.id]),
            {'status': 'in_progress'}
        )
        self.assertEqual(response.status_code, 302)  # Redirect after success
        
        # Verify status was updated
        request.refresh_from_db()
        self.assertEqual(request.status, 'in_progress')

    def test_unauthorized_access(self):
        # Create another user
        other_user = User.objects.create_user(
            username='otheruser',
            password='testpass123'
        )
        
        # Create a request for the other user
        request = ServiceRequest.objects.create(
            user=other_user,
            title='Other User Request',
            description='Test Description'
        )
        
        # Try to access the request
        response = self.client.get(reverse('request_detail', args=[request.id]))
        self.assertEqual(response.status_code, 404)  # Should not be found
