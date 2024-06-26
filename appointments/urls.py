from django.urls import path
from .views import AppointmentListView, AppointmentCreateView, PatientAppointmentListView, DoctorAppointmentListView, AppointmentUpdateView

urlpatterns = [
    path('appointments/list/', AppointmentListView.as_view(), name='appointment-list'),
    path('appointments/create/<int:doctor_id>/', AppointmentCreateView.as_view(), name='appointment-create'),
    path('patient/appointments/', PatientAppointmentListView.as_view(), name='patient-appointments'),
    path('doctor/appointments/', DoctorAppointmentListView.as_view(), name='doctor-appointments'),
    path('appointments/update/<int:pk>/', AppointmentUpdateView.as_view(), name='appointment-update'),  # Nueva ruta para actualizar citas
]