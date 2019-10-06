from rest_framework import serializers
from .models import Plat,Personnel,Category,Place,Poste,Ingredient
from configuration.models import Social

class PlatSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Plat
        fields = '__all__'
        depth = 1
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
class PersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personnel
        fields = '__all__'
        depth = 1
class PosteSerializer(serializers.ModelSerializer):
    poste_personnel=PersonnelSerializer(many=True)
    class Meta:
        model = Poste
        fields = '__all__'
class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'
    depth = 1

class SocialSerializer(serializers.ModelSerializer):
    social_personnel = PersonnelSerializer(many=True,read_only=True)
    class Meta:
        model = Social
        field = '__all__'
