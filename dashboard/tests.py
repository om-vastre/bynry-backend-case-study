from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from service_requests.models import ServiceRequest
from .models import SupportStaff, RequestAssignment

class DashboardTests(TestCase):
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(
            username='teststaff',
            password='testpass123'
        )
        # Create support staff
        self.staff = SupportStaff.objects.create(
            user=self.user,
            department='Technical Support'
        )
        # Create test client
        self.client = Client()
        self.client.login(username='teststaff', password='testpass123')

    def test_dashboard_home(self):
        response = self.client.get(reverse('dashboard_home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/home.html')

    def test_assign_request(self):
        # Create a test service request
        service_request = ServiceRequest.objects.create(
            user=self.user,
            title='Test Request',
            description='Test Description',
            status='pending'
        )
        
        # Test assigning request
        response = self.client.post(
            reverse('assign_request', args=[service_request.id]),
            {'notes': 'Test assignment'}
        )
        self.assertEqual(response.status_code, 302)  # Redirect after success
        
        # Verify assignment was created
        assignment = RequestAssignment.objects.get(service_request=service_request)
        self.assertEqual(assignment.support_staff, self.staff)
        self.assertEqual(assignment.notes, 'Test assignment')

    def test_staff_availability(self):
        # Test updating availability
        response = self.client.post(
            reverse('staff_availability'),
            {'is_available': 'true'}
        )
        self.assertEqual(response.status_code, 302)  # Redirect after success
        
        # Verify availability was updated
        self.staff.refresh_from_db()
        self.assertTrue(self.staff.is_available)

    def test_non_staff_access(self):
        # Create a regular user
        regular_user = User.objects.create_user(
            username='regularuser',
            password='testpass123'
        )
        self.client.login(username='regularuser', password='testpass123')
        
        # Try to access dashboard
        response = self.client.get(reverse('dashboard_home'))
        self.assertEqual(response.status_code, 302)  # Should redirect
