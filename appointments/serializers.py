from rest_framework import serializers
from .models import Appointment, Doctor, Patient

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['name', 'last_name']
        

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['name', 'last_name']
        

class AppointmentSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer(read_only=True)
    patient = PatientSerializer(read_only=True)
    doctor_id = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all(), source='doctor', write_only=True)
    is_active_display = serializers.SerializerMethodField()
    
    class Meta:
        model = Appointment
        fields = ['id', 'doctor', 'doctor_id', 'patient', 'date', 'observation', 'time', 'is_active', 'is_active_display']
    
    def get_is_active_display(self, obj):
        return obj.get_is_active_display()

    def validate(self, data):
        if self.instance and self.instance.patient != self.context['request'].user.patient:
            raise serializers.ValidationError("No tienes permiso para editar esta cita.")
        return data

def create(self, validated_data):
    patient = self.context['request'].user.patient
    validated_data.pop('patient', None)  
    return Appointment.objects.create(patient=patient, **validated_data)


class AppointmentCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'doctor', 'patient', 'date', 'observation', 'time', 'is_active']

    def validate(self, data):
        if self.instance and self.instance.patient != self.context['request'].user.patient:
            raise serializers.ValidationError("No tienes permiso para editar esta cita.")
        return data
