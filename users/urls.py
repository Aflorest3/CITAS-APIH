from django.urls import path
from .views import PatientView, DoctorView, DoctorListView, DoctorCreateView, PatientCreateView, PatientListView

urlpatterns = [
    path('patients/<int:pk>/', PatientView.as_view(), name='patient-detail'),
    path('patients/create/', PatientCreateView.as_view(), name='patient-create'),
    path('patients/', PatientListView.as_view(), name='patient-list'),
    path('doctors/<int:pk>/', DoctorView.as_view(), name='doctor-detail'),
    path('doctors/create/', DoctorCreateView.as_view(), name='doctor-create'),
    path('doctors/', DoctorListView.as_view(), name='doctor-list'),
]

