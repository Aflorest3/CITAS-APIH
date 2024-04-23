from django.contrib.auth import get_user_model
from rest_framework import serializers
from users.models import Patient, Doctor

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'name', 'last_name', 'gender', 'phone', 'is_staff', 'is_active']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user

class DoctorSerializer(serializers.ModelSerializer):
    class Meta(UserSerializer.Meta):
        model = Doctor
        fields = UserSerializer.Meta.fields + ['speciality', 'no_collegiate']

class PatientSerializer(serializers.ModelSerializer):
    class Meta(UserSerializer.Meta):
        model = Patient
        fields = UserSerializer.Meta.fields + ['no_dpi']