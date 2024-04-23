from rest_framework import generics
from rest_framework.generics import CreateAPIView
from users.serializers import PatientSerializer, DoctorSerializer
from users.models import Patient, Doctor

class PatientView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

class DoctorView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()

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

class PatientCreateView(CreateAPIView):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()
