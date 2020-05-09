from django.shortcuts import render
from django.http import JsonResponse

def test_route(request):
	return JsonResponse({'message': 'route is working'})
