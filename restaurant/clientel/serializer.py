from rest_framework import serializers
from .models import Reservation,Temoignage
from resto.models import Plat,Ingredient,Category
class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
        depth = 2

class PlatSerializer(serializers.ModelSerializer):
    plat_reserver=ReservationSerializer(many=True)
    class Meta:
        model = Plat
        fields = '__all__'
        # depth = 1
        
class IngredientSerializer(serializers.ModelSerializer):
    ingrediant_plat=PlatSerializer(many=True)
    class Meta:
        model = Ingredient
        fields = '__all__'
        
class CategorySerializer(serializers.ModelSerializer):
    category_client=PlatSerializer(many=True)
    class Meta:
        model = Category
        fields = '__all__'

class TemoignageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temoignage
        fields = '__all__'
