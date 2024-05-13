from rest_framework import generics
from rest_framework.generics import CreateAPIView
from users.serializers import PatientSerializer, DoctorSerializer
from users.models import Patient, Doctor

class PatientView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()
    
    def perform_update(self, serializer):
        password = self.request.data.get('password')
        instance = serializer.save()
        if password:
            instance.set_password(password)
            instance.save()
            

class DoctorView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
    
    def perform_update(self, serializer):
        password = self.request.data.get('password')
        instance = serializer.save()
        if password:
            instance.set_password(password)
            instance.save()
    
    
class PatientListView(generics.ListAPIView):
    serializer_class = PatientSerializer
    
    def get_queryset(self):
        return Patient.objects.all()
    
class DoctorListView(generics.ListAPIView):
    serializer_class = DoctorSerializer
    
    def get_queryset(self):
        return Doctor.objects.all()

class DoctorCreateView(CreateAPIView):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
    
    def perform_create(self, serializer):
        password = self.request.data.get('password')
        instance = serializer.save()
        if password:
            instance.set_password(password)
            instance.save()

class PatientCreateView(CreateAPIView):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()
    
    def perform_create(self, serializer):
        password = self.request.data.get('password')
        instance = serializer.save()
        if password:
            instance.set_password(password)
            instance.save()
