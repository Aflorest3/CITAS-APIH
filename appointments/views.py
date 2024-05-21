from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Appointment, Doctor
from .serializers import AppointmentSerializer, DoctorDetailSerializer, PatientDetailSerializer

class AppointmentListView(generics.ListAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    #permission_classes = [IsAuthenticated]

class AppointmentCreateView(generics.CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        doctor_id = self.kwargs.get('doctor_id')
        doctor = Doctor.objects.get(id=doctor_id)
        serializer.save(patient=self.request.user.patient, doctor=doctor)

class AppointmentUpdateView(generics.UpdateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()

class PatientAppointmentListView(generics.ListAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Appointment.objects.filter(patient=user.patient)

class DoctorAppointmentListView(generics.ListAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Appointment.objects.filter(doctor=user.doctor)