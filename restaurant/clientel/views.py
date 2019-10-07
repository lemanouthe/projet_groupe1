from rest_framework import viewsets
from .serializer import ReservationSerializer, TemoignageSerializer
from .models import Reservation , Temoignage

class ReservationViewset(viewsets.ModelViewSet):
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.filter(status=True)

class TemoignageViewset(viewsets.ModelViewSet):
    serializer_class = TemoignageSerializer
    queryset = Temoignage.objects.filter(status=True)
    
#gestion de configuration
from django.shortcuts import render, redirect
from configuration.models import  ReserveConfig

reservConf = ReserveConfig.objects.filter(status=True)


data = {
    'reservConf': reservConf,
}

def reservations(request):
    return render(request, 'pages/clientele/reservation.html', data)
