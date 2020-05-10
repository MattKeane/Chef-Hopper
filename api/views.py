from django.shortcuts import render
from django.http import JsonResponse
from scraper.scraper import *

def test_route(request):
	return JsonResponse({'message': 'route is working'})

def get_recipes(request, query):
	urls = get_all_recipes_urls(query)
	return JsonResponse({"message": urls})	
