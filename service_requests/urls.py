from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_request, name='create_request'),
    path('list/', views.request_list, name='request_list'),
    path('detail/<int:pk>/', views.request_detail, name='request_detail'),
] 