from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import AppointmentViewSet, AppointmentFilterByDateView

urlpatterns = [
    path('create/', AppointmentViewSet.as_view({'post': 'create'}), name='appointment-create'),
    path('<int:pk>/', AppointmentViewSet.as_view({'get': 'retrieve'}), name='appointment-detail'),
    path('', AppointmentViewSet.as_view({'get': 'list'}), name='appointment-list'),
    path('filter-by-date/', AppointmentFilterByDateView.as_view(), name='appointment-filter-by-date'),
]