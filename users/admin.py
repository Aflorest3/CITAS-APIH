from django.contrib import admin
from users.models import User, Doctor, Patient
from appointments.models import Appointment

# Register your models here.

admin.site.register(User)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)


