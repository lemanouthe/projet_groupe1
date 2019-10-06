
from django.urls import path
from .models import Reservation , Temoignage
from rest_framework.routers import DefaultRouter
from .views import ReservationViewset , TemoignageViewset

router = DefaultRouter()
router.register(r'reservation',ReservationViewset,base_name='reserve')
router.register(r'temoignage',TemoignageViewset,base_name='temoignages')

urlpatterns = [
]

urlpatterns += router.urls