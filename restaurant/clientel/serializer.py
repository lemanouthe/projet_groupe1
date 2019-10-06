from rest_framework import serializers
from .models import Reservation,Temoignage

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

class TemoignageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temoignage
        fields = '__all__'