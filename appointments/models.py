from django.db import models
from django.conf import settings
from users.models import Patient, Doctor

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    observation = models.TextField()
    time = models.TimeField()
    ACTIVE_CHOISES = (
        (0, 'EN PROCESO'),
        (1, 'PROCESADA'),
        (2, 'CONFIRMADA'),
        (3, 'CANCELADA'),
        (4, 'REPROGRAMADA'),
        (5, 'FINALIZADA'),
    )
    is_active = models.SmallIntegerField(default=0, choices=ACTIVE_CHOISES)



    @classmethod
    def citas_por_fecha(cls, fecha):
        return cls.objects.filter(date=fecha)


    def str(self):
        return str(self.id)