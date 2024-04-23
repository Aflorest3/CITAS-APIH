from django.db import models
from django.conf import settings

class Appointment(models.Model):
    users = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    observation = models.TextField()
    time = models.TimeField()
    is_active = models.BooleanField(default=True)


    @classmethod
    def citas_por_fecha(cls, fecha):
        return cls.objects.filter(date=fecha)
    
    
    def __str__(self):
        return str(self.id)
