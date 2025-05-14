from django.db import models
from django.contrib.auth.models import User
from service_requests.models import ServiceRequest

class SupportStaff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    is_available = models.BooleanField(default=True)
    assigned_requests = models.ManyToManyField(ServiceRequest, related_name='assigned_staff', blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.department}"

class RequestAssignment(models.Model):
    service_request = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE)
    support_staff = models.ForeignKey(SupportStaff, on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)

    class Meta:
        unique_together = ('service_request', 'support_staff')

    def __str__(self):
        return f"{self.service_request.title} - {self.support_staff.user.username}"
