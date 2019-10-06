from rest_framework import serializers
from .models import Social

class SocialSerializer(serializers.ModelSerializer):
    social_personnel = serializer.PersonnelSerializer(many=True)
    class Meta:
        model = Social
        field = '__all__'