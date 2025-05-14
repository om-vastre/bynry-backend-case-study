from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ServiceRequest
from .forms import ServiceRequestForm, ServiceRequestUpdateForm

# Create your views here.

@login_required
def create_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = request.user
            service_request.save()
            messages.success(request, 'Service request submitted successfully!')
            return redirect('request_list')
    else:
        form = ServiceRequestForm()
    return render(request, 'service_requests/create_request.html', {'form': form})

@login_required
def request_list(request):
    requests = ServiceRequest.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'service_requests/request_list.html', {'requests': requests})

@login_required
def request_detail(request, pk):
    service_request = get_object_or_404(ServiceRequest, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ServiceRequestUpdateForm(request.POST, instance=service_request)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service request updated successfully!')
            return redirect('request_detail', pk=pk)
    else:
        form = ServiceRequestUpdateForm(instance=service_request)
    return render(request, 'service_requests/request_detail.html', {
        'service_request': service_request,
        'form': form
    })
