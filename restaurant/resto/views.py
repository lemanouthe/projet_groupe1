from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly,BasePermission,SAFE_METHODS
from .serializer import PlatSerializer,PosteSerializer,IngredientSerializer,PersonnelSerializer,CategorySerializer,PlaceSerializer
from .models import Plat,Poste,Ingredient,Personnel,Place,Category
from random import randint
from django.http import	JsonResponse
import faker

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class PlatViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated|ReadOnly]
    serializer_class = PlatSerializer
    queryset = Plat.objects.all()
class PosteViewset(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser|ReadOnly]
    serializer_class = PosteSerializer
    queryset = Poste.objects.all()
class CategoryViewset(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser|ReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
class PersonnelViewset(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser|ReadOnly]
    serializer_class = PersonnelSerializer
    queryset = Personnel.objects.all()
class PlaceViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated|ReadOnly]
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()
class IngredientViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated|ReadOnly]
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
