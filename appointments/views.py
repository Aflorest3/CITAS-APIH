from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Appointment, Doctor
from .serializers import AppointmentSerializer
from rest_framework.exceptions import NotFound

class AppointmentListView(generics.ListAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

class AppointmentCreateView(generics.CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        doctor_id = self.kwargs.get('doctor_id')
        
        # Validar que el doctor exista
        try:
            doctor = Doctor.objects.get(id=doctor_id)
        except Doctor.DoesNotExist:
            raise NotFound(f'Doctor with id {doctor_id} does not exist')

        # Verificar que el usuario tenga un objeto Patient asociado
        if not hasattr(self.request.user, 'patient'):
            raise NotFound('User does not have a patient profile associated')

        # Excluye patient y doctor de validated_data para evitar duplicación
        serializer.validated_data.pop('patient', None)
        serializer.validated_data.pop('doctor', None)

        # Guarda el serializer con los valores adecuados
        serializer.save(patient=self.request.user.patient, doctor=doctor)

class AppointmentUpdateView(generics.UpdateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

class PatientAppointmentListView(generics.ListAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if not hasattr(user, 'patient'):
            raise NotFound('User does not have a patient profile associated')
        return Appointment.objects.filter(patient=user.patient)

class DoctorAppointmentListView(generics.ListAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if not hasattr(user, 'doctor'):
            raise NotFound('User does not have a doctor profile associated')
        return Appointment.objects.filter(doctor=user.doctor)
