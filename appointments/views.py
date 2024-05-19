from rest_framework import generics
from .models import Appointment, Doctor
from .serializers import AppointmentSerializer
from rest_framework.permissions import IsAuthenticated

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


class PatientAppointmentListView(generics.ListAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Esta vista debería devolver una lista de todas las citas
        para el paciente que está actualmente autenticado.
        """
        user = self.request.user
        return Appointment.objects.filter(patient=user.patient)

class DoctorAppointmentListView(generics.ListAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Esta vista debería devolver una lista de todas las citas
        para el doctor que está actualmente autenticado.
        """
        user = self.request.user
        return Appointment.objects.filter(doctor=user.doctor)