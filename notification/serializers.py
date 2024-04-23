from rest_framework import serializers
from .models import Notificationlyst

class NotificationlystSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificationlyst
        fields = ['id','appointment','message', 'date_time']