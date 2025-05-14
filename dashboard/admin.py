from django.contrib import admin
from .models import SupportStaff, RequestAssignment

@admin.register(SupportStaff)
class SupportStaffAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'is_available')
    list_filter = ('department', 'is_available')
    search_fields = ('user__username', 'department')

@admin.register(RequestAssignment)
class RequestAssignmentAdmin(admin.ModelAdmin):
    list_display = ('service_request', 'support_staff', 'assigned_at')
    list_filter = ('assigned_at', 'support_staff__department')
    search_fields = ('service_request__title', 'support_staff__user__username', 'notes')
    date_hierarchy = 'assigned_at'
