from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_home, name='dashboard_home'),
    path('assign/<int:request_id>/', views.assign_request, name='assign_request'),
    path('availability/', views.staff_availability, name='staff_availability'),
] 