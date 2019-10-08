from rest_framework import viewsets
from .serializer import ReservationSerializer, TemoignageSerializer
from .models import Reservation , Temoignage
from django.shortcuts import render

class ReservationViewset(viewsets.ModelViewSet):
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.filter(status=True)

class TemoignageViewset(viewsets.ModelViewSet):
    serializer_class = TemoignageSerializer
    queryset = Temoignage.objects.filter(status=True)
    
    
def reservation(request):
    return render(request, 'pages/clientele/reservation.html')
    