from .views import PlatViewset,CategoryViewset,PlaceViewset,IngredientViewset,PosteViewset,PersonnelViewset
from rest_framework.routers import DefaultRouter
from .views import giveIngredient,giveSocial
from django.urls import path
router = DefaultRouter()
router.register(r'plats', PlatViewset, basename='plat')
router.register(r'category', CategoryViewset, basename='category')
router.register(r'places', PlaceViewset, basename='place')
router.register(r'ingredients', IngredientViewset, basename='ingredient')
router.register(r'postes', PosteViewset, basename='poste')
router.register(r'personnels', PersonnelViewset, basename='personnel')


urlpatterns = [
    path('fake',giveSocial,name='fake')
]
urlpatterns += router.urls