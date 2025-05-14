from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.db.models import Count
from service_requests.models import ServiceRequest
from .models import SupportStaff, RequestAssignment

def is_support_staff(user):
    return hasattr(user, 'supportstaff')

@login_required
@user_passes_test(is_support_staff)
def dashboard_home(request):
    # Get statistics
    total_requests = ServiceRequest.objects.count()
    pending_requests = ServiceRequest.objects.filter(status='pending').count()
    in_progress_requests = ServiceRequest.objects.filter(status='in_progress').count()
    resolved_requests = ServiceRequest.objects.filter(status='resolved').count()

    # Get staff's assigned requests
    staff = request.user.supportstaff
    assigned_requests = staff.assigned_requests.all().order_by('-created_at')

    context = {
        'total_requests': total_requests,
        'pending_requests': pending_requests,
        'in_progress_requests': in_progress_requests,
        'resolved_requests': resolved_requests,
        'assigned_requests': assigned_requests,
    }
    return render(request, 'dashboard/home.html', context)

@login_required
@user_passes_test(is_support_staff)
def assign_request(request, request_id):
    service_request = get_object_or_404(ServiceRequest, id=request_id)
    staff = request.user.supportstaff

    if request.method == 'POST':
        notes = request.POST.get('notes', '')
        RequestAssignment.objects.create(
            service_request=service_request,
            support_staff=staff,
            notes=notes
        )
        staff.assigned_requests.add(service_request)
        service_request.status = 'in_progress'
        service_request.save()
        messages.success(request, 'Request assigned successfully!')
        return redirect('dashboard_home')

    return render(request, 'dashboard/assign_request.html', {
        'service_request': service_request
    })

@login_required
@user_passes_test(is_support_staff)
def staff_availability(request):
    staff = request.user.supportstaff
    if request.method == 'POST':
        is_available = request.POST.get('is_available') == 'true'
        staff.is_available = is_available
        staff.save()
        status = 'available' if is_available else 'unavailable'
        messages.success(request, f'You are now {status}')
        return redirect('dashboard_home')

    return render(request, 'dashboard/staff_availability.html', {
        'staff': staff
    })
