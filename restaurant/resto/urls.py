
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('special_dishes/', views.special_dishes, name='special_dishes'),
    path('team/', views.team, name='team'),
]
