from rest_framework import serializers
from .models import Appointment, Doctor, Patient

class DoctorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'last_name']

class PatientDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['name', 'last_name']

class AppointmentSerializer(serializers.ModelSerializer):
    doctor = DoctorDetailSerializer(read_only=True)
    patient = PatientDetailSerializer(read_only=True)
    is_active_display = serializers.SerializerMethodField()
    doctor_id = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = Appointment
        fields = ['id', 'doctor', 'patient', 'date', 'observation', 'time', 'is_active', 'is_active_display', 'doctor_id']

    def get_is_active_display(self, obj) -> str:
        return obj.get_is_active_display()

    def create(self, validated_data):
        # Excluye patient y doctor de validated_data para evitar duplicación
        validated_data.pop('patient', None)
        validated_data.pop('doctor', None)
        
        # Recupera patient y doctor del contexto
        patient = self.context['request'].user.patient
        doctor_id = validated_data.pop('doctor_id', None)
        doctor = Doctor.objects.get(id=doctor_id) if doctor_id else None
        
        # Crea la cita con los valores adecuados
        return Appointment.objects.create(patient=patient, doctor=doctor, **validated_data)

    def update(self, instance, validated_data):
        # Maneja doctor_id de manera adecuada durante la actualización
        doctor_id = validated_data.pop('doctor_id', None)
        if doctor_id:
            instance.doctor = Doctor.objects.get(id=doctor_id)
        return super().update(instance, validated_data)

    def validate(self, data):
        # Valida que el paciente sea el correcto
        if self.instance and self.instance.patient != self.context['request'].user.patient:
            raise serializers.ValidationError("No tienes permiso para editar esta cita.")
        return data
