from .views import PlatViewset,CategoryViewset,PlaceViewset,IngredientViewset,PosteViewset,PersonnelViewset
from rest_framework.routers import DefaultRouter
from .views import giveIngredient,giveSocial,giveDay,UserCreate

from django.urls import path
router = DefaultRouter()
router.register(r'plats', PlatViewset, basename='plat')
router.register(r'category', CategoryViewset, basename='category')
router.register(r'places', PlaceViewset, basename='place')
router.register(r'ingredients', IngredientViewset, basename='ingredient')
router.register(r'postes', PosteViewset, basename='poste')
router.register(r'personnels', PersonnelViewset, basename='personnel')
from . import views
app_name='resto'

urlpatterns = [
    path('fake',giveSocial,name='fake'),

    path('restaurant/', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('special/', views.special, name='special'),
    path('team/', views.team, name='team'),
]
urlpatterns += router.urls