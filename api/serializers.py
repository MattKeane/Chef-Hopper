from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.Serializer):
	url = serializers.CharField(max_length=511)
	title = serializers.CharField(max_length=255)
	ingredients = serializers.ListField(child=serializers.CharField(max_length=255))
	instructions = serializers.ListField(child=serializers.CharField(max_length=255))