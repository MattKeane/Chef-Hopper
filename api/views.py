from django.shortcuts import render
from django.http import JsonResponse
from scraper.scraper import *

def test_route(request):
	return JsonResponse({'message': 'route is working'})

def get_recipes(request, query):
	recipes = scrape_recipes(query, 1)
	return JsonResponse({
		"data": recipes,
		"message": str(len(recipes)) + " recipes returned",
		"status": 200
		})	
