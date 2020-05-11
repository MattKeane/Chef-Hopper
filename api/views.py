from django.shortcuts import render
from django.http import JsonResponse
from scraper.scraper import scrape_recipes
from .models import Search, Recipe, RecipeSerializer

def test_route(request):
	return JsonResponse({'message': 'route is working'})

def search(request, query):
	query = query.replace("+", " ")
	# recipes = scrape_recipes(query, 1)
	# return JsonResponse({
	# 	"data": recipes,
	# 	"message": str(len(recipes)) + " recipes returned",
	# 	"status": 200
	# 	})	
	# models.Recipe.objects.filter()

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
			print(obj.id)
		return JsonResponse({
			"data": recipes,
			"status": 200
			})
	else:
		return JsonResponse({
			"message": "already exists in database"
			})