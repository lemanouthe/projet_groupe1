from rest_framework import viewsets
# from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly,BasePermission,SAFE_METHODS
from .serializer import PlatSerializer,PosteSerializer,IngredientSerializer,PersonnelSerializer,CategorySerializer,PlaceSerializer,UserSerializer
from .models import Plat,Poste,Ingredient,Personnel,Place,Category
from django.contrib.auth.models import User
from random import randint
from django.http import	JsonResponse
from rest_framework import filters
from django.shortcuts import render
import faker
from configuration.models import About,Presentation

# class ReadOnly(BasePermission):
#     def has_permission(self, request, view):
#         return request.method in SAFE_METHODS
class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])

class UserCreate(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    # permission_classes = [IsAdminUser|ReadOnly]
    serializer_class=UserSerializer
    def get_queryset(self):
        queryset = User.objects.filter()
        return queryset
class PlatViewset(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    # permission_classes = [IsAuthenticated|ReadOnly]
    serializer_class = PlatSerializer
    queryset = Plat.objects.all()
class PosteViewset(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    # permission_classes = [IsAdminUser|ReadOnly]
    serializer_class = PosteSerializer
    queryset = Poste.objects.all()
class CategoryViewset(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    # permission_classes = [IsAdminUser|ReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
class PersonnelViewset(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    # permission_classes = [IsAdminUser|ReadOnly]
    serializer_class = PersonnelSerializer
    queryset = Personnel.objects.all()
class PlaceViewset(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    # permission_classes = [IsAuthenticated|ReadOnly]
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()
class IngredientViewset(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    # permission_classes = [IsAuthenticated|ReadOnly]
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

def giveDay(request):
    from configuration.models import Day    
    day = Day.objects.filter(status=True)
    plat = Plat.objects.filter(status=True)

    for plt in plat:
        for d in range(0,randint(1,5)):
            plt.days.add(day[randint(0,6)])
        plt.save()
    return JsonResponse({'succees':True})


def home(request):
    return render(request, 'pages/resto/index.html', data, context=RequestContext(request))


def index(request):
    return render(request, 'pages/resto/index.html', data)
################### JINJA views #######################

def index(request):
    about = About.objects.all()
    presentation = Presentation.objects.all()
    data={
        'about':about,
        'presentation':presentation,
    }
    return render(request,'pages/resto/index.html',data)
def menu(request):
    return render(request, 'pages/resto/menu.html')

def team(request):
    return render(request, 'pages/resto/team.html')

def special(request):
    return render(request,'pages/resto/special_dishes.html')