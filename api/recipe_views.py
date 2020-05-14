from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .models import Recipe, Profile
from django.contrib.auth import authenticate
from .serializers import RecipeSerializer

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

def get_saved_recipes(request):
	if request.user.is_authenticated:
		saved_recipes = request.user.profile.saved_recipe.all()
		saved_recipes = [RecipeSerializer(recipe).data for recipe in saved_recipes]
		return JsonResponse({
			"message": "Returned " + str(len(saved_recipes)) + " recipes.",
			"data": saved_recipes,
			"status": 200
		})
	else:
		return JsonResponse({
			"message": "You must be logged in to do that",
			"data": {},
			"status": 401
		})


def remove_saved_recipe(request, recipe_id):
	if request.user.is_authenticated:
		recipe_to_remove = Recipe.objects.get(id=recipe_id)
		request.user.profile.saved_recipe.remove(recipe_to_remove)
		return JsonResponse({
			"message": "Saved recipe removed",
			"data": {},
			"status": 200
		})
	else:
		return JsonResponse({
			"message": "You must be logged in to do that",
			"data": {},
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

