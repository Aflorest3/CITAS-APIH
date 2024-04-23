from rest_framework import viewsets
from .models import Notificationlyst
from .serializers import NotificationlystSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationlystSerializer
    queryset = Notificationlyst.objects.all()