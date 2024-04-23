from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Appointment
from rest_framework.views import APIView
from .serializers import AppointmentSerializer
from datetime import datetime

class AppointmentViewSet(viewsets.ModelViewSet):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()

    def perform_create(self, serializer):
        users_id = self.request.data.get('users')
        if users_id:
            serializer.save(users_id=users_id)
        else:
            return Response({"error": "User ID is required"}, status=status.HTTP_400_BAD_REQUEST)

class AppointmentFilterByDateView(APIView):
    def get(self, request):
        # Obtenemos la fecha de la solicitud (si se proporciona)
        fecha_str = request.query_params.get('fecha', None)
        print(f"Fecha recibida: {fecha_str}")  # Imprime la fecha recibida
        if fecha_str:
            # Convertimos la cadena de texto a un objeto de fecha
            fecha = datetime.strptime(fecha_str, '%Y-%m-%d').date()
            print(f"Fecha convertida: {fecha}")  # Imprime la fecha convertida
            # Filtramos las citas por fecha si se proporciona una fecha válida
            queryset = Appointment.objects.filter(date=fecha)
            print(f"Citas filtradas: {queryset}")  # Imprime las citas filtradas
            serializer = AppointmentSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response({"error": "Fecha parameter is required"}, status=status.HTTP_400_BAD_REQUEST)


    # ruta para usar el filtro http://127.0.0.1:8000/appointments/?fecha=2024-04-22