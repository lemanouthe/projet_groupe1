from rest_framework import serializers
from .models import Plat,Personnel,Category,Place,Poste,Ingredient
from configuration.models import Social
from django.contrib.auth.models import User

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

class UserSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
