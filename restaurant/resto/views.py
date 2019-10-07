from rest_framework import viewsets
from .serializer import PlatSerializer,PosteSerializer,IngredientSerializer,PersonnelSerializer,CategorySerializer,PlaceSerializer
from .models import Plat,Poste,Ingredient,Personnel,Place,Category
from random import randint
from django.http import	JsonResponse
import faker

class PlatViewset(viewsets.ModelViewSet):
    
    serializer_class = PlatSerializer
    queryset = Plat.objects.all()
class PosteViewset(viewsets.ModelViewSet):
    
    serializer_class = PosteSerializer
    queryset = Poste.objects.all()
class CategoryViewset(viewsets.ModelViewSet):
    
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
class PersonnelViewset(viewsets.ModelViewSet):
    
    serializer_class = PersonnelSerializer
    queryset = Personnel.objects.all()
class PlaceViewset(viewsets.ModelViewSet):
    
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()
class IngredientViewset(viewsets.ModelViewSet):
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()




######################## faker view 

def giveIngredient(request):
    
    ingredient = Ingredient.objects.filter(status=True)
    plat = Plat.objects.filter(status=True)

    for pl in plat:
        for cp in range(0,randint(1,5)):
            pl.ingredient.add(ingredient[randint(0,149)])
        pl.save()
    return JsonResponse({'succees':True})

def giveSocial(request):
    from configuration.models import Social    
    sociaux = Social.objects.filter(status=True)
    personnes = Personnel.objects.filter(status=True)

    for prs in personnes:
        for sc in range(0,randint(1,3)):
            prs.social.add(sociaux[randint(0,3)])
        prs.save()
    return JsonResponse({'succees':True})


#dynamisation des config
from configuration.models import Presentation, ReserveConfig, About
from django.shortcuts import render, redirect


present = Presentation.objects.filter(status=True)
reservat = ReserveConfig.objects.filter(status=True)
about = About.objects.filter(status=True)


data = {
    'present': present,
    'reservat': reservat,
    'about': about,
}

def index(request):
    return render(request, 'pages/resto/index.html', data)