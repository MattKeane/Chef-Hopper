from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .models import Recipe, Profile
from django.contrib.auth import authenticate

def save_recipe(request, recipe_id):
	if request.user.is_authenticated:
		recipe_to_save = Recipe.objects.get(id=recipe_id)
		request.user.profile.saved_recipe.add(recipe_to_save)
		return JsonResponse({
			"message": "Recipe saved",
			"data": {},
			"status": 200
		})
	else:
		return JsonResponse({
			"message": "You must be logged in to do that",
			"data" : {},
			"status": 401
			})

def test_recipe_views(request):
	if request.user.is_authenticated:
		test_recipe = Recipe.objects.get(id=70)
		current_user = request.user.profile.saved_recipe
		current_user.add(test_recipe)
		return JsonResponse({
			"message": "test works"
			})
	else:
		return JsonResponse({
			"message": "test doesn't work"
			})