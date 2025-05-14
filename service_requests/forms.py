from django import forms
from .models import ServiceRequest

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ('title', 'description', 'attachment')
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class ServiceRequestUpdateForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ('status',) 