from rest_framework import serializers
from .models import Appointment, Doctor, Patient

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['name', 'last_name']
        read_only_fields = ['name', 'last_name']

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['name', 'last_name']
        read_only_fields = ['name', 'last_name']

class AppointmentSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer(read_only=True)
    patient = PatientSerializer(read_only=True)

    class Meta:
        model = Appointment
        fields = ['id', 'doctor', 'patient', 'date', 'observation', 'time', 'is_active']
        read_only_fields = ['doctor', 'patient']

    def create(self, validated_data):
        patient = self.context['request'].user.patient
        return Appointment.objects.create(patient=patient, **validated_data)