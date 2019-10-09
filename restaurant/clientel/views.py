from rest_framework import viewsets,filters
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly,BasePermission,SAFE_METHODS
from .serializer import ReservationSerializer, TemoignageSerializer
from .models import *
from django.shortcuts import render
from django.core.validators import validate_email
from django.http import HttpResponse


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])


class ReservationViewset(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    permission_classes = []
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.filter(status=True)

class TemoignageViewset(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = TemoignageSerializer
    queryset = Temoignage.objects.filter(status=True)
    
    
def reservation(request):
    nom = request.POST.get('nom')
    email = request.POST.get('email')
    numero = request.POST.get('numero')
    date = request.POST.get('date')
    heure = request.POST.get('heure')
    personne = request.POST.get('personne')
    message = request.POST.get('message')
    
    # print(nom,email,numero,date,heure,personne,message)
    try:
        validate_email(email)
        is_email=True
        if is_email and nom is not None and numero is not None and date is not None and heure is not None and personne is not None and message is not None:
            h = Reservation(nom=nom,email=email,numero=numero,date=date,heure=heure,personne=personne,message=message)
            h.save()
    except:
        print('remplir ce formulaire')
    
    return render(request, 'pages/clientele/reservation.html')