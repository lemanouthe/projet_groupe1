from rest_framework import viewsets,filters
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly,BasePermission,SAFE_METHODS
from .serializer import ReservationSerializer, TemoignageSerializer
from .models import *
from configuration.models import  ReserveConfig
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
    reservConf = ReserveConfig.objects.filter(status=True)
    
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
    except:
        pass
    if request.method == "POST":
        if nom == "" and email == "" and numero == "" and date == "" and heure == "" and personne == "" and message == "":
            messages.warning(request, "Erreur veuilllez remplir le formulaire")
        else:
            h = Reservation(nom=nom, email=email, numero=numero, date=date, heure=heure, personne=personne, message=message)
            h.save()


    data = {
        'reservConf': reservConf,
    }

    return render(request, 'pages/clientele/reservation.html', data)
