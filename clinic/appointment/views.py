from rest_framework import viewsets
from .models import Appointment
from .serializers import AppointmentSerializer 

# Create your views here.
class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        pacient = self.request.query_params.get('pacient')
        doctor = self.request.query_params.get('doctor')

        if pacient:
            queryset = queryset.filter(pacient=pacient)

        if doctor:
            queryset = queryset.filter(doctor=doctor)
            
        return queryset

