from django.shortcuts import render
from django.http import JsonResponse
from scraper.scraper import scrape_recipes
from rest_framework.renderers import JSONRenderer
from .models import Search, Recipe
from .serializers import RecipeSerializer

def test_route(request):
	return JsonResponse({'message': 'route is working'})

def search(request, query):
	query = query.replace("+", " ")
	existing_results = Search.objects.filter(search_term=query)
	if len(existing_results) == 0:
		recipes = scrape_recipes(query, 5)
		for recipe in recipes:
			obj, created = Recipe.objects.get_or_create(
				url=recipe["url"],
				defaults={
					"title": recipe["title"],
					"ingredients": recipe["ingredients"],
					"instructions": recipe["instructions"]
				})
			Search.objects.create(
				search_term=query,
				recipe=obj
			)
		return JsonResponse({
			"message": "recipes added to database",
			"data": recipes,
			"status": 200
			})
	else:
		recipes = [RecipeSerializer(result.recipe).data for result in existing_results]
		return JsonResponse({
			"message": "recipes retrieved from database",
			"data": recipes,
			"status": 200
			})