from django.db import models
from django.conf import settings
from appointments.models import Appointment

class Notificationlyst(models.Model):
    appointment = models.ForeignKey(Appointment,on_delete=models.CASCADE )
    message = models.CharField(max_length=255)
    date_time = models.DateTimeField()

    def __str__(self):
        return f"{self.appointment.id}"