from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from scraper.scraper import scrape_recipes
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from .models import Search, Recipe, Profile
from .serializers import RecipeSerializer, UserSerializer


def test_route(request):
	return JsonResponse({'message': 'route is working'})

def search(request, query):
	query = query.replace("+", " ")
	existing_results = Search.objects.filter(search_term=query)
	if len(existing_results) == 0:
		recipes = []
		new_recipes = scrape_recipes(query, 5)
		for recipe in new_recipes:
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
			recipes.append(RecipeSerializer(obj).data)
		if recipes:
			return JsonResponse({
				"message": "recipes added to database",
				"data": recipes,
				"status": 201
				})
		else:
			return JsonResponse({
				"message": "Search returned no results.",
				"data": [],
				"status": 200
				})
	else:
		recipes = [RecipeSerializer(result.recipe).data for result in existing_results]
		return JsonResponse({
			"message": "recipes retrieved from database",
			"data": recipes,
			"status": 200
			})

@api_view(["POST"])
def register(request):
	try:
		user = User.objects.create_user(
			username=request.data["username"],
			email=request.data["email"],
			password=request.data["password"]
		)
		profile = Profile.objects.create(
			user=user
		)
		login(request, user)
		return JsonResponse({
			"message": "User created.",
			"data": UserSerializer(user).data,
			"status": 201
			}) 
	except IntegrityError:
		return JsonResponse({
			"message": "User already exists",
			"status": 401
			})

def get_logged_in_user(request):
	if request.user.is_authenticated:
		return JsonResponse({
			"message": "user is logged in",
			"data": UserSerializer(request.user).data,
			"status": 200
			})
	else:
		return JsonResponse({
			"data": {},
			"message": "No user is currently logged in",
			"status": 401
			})

def log_out(request):
	logout(request)
	return JsonResponse({
		"data": {},
		"message": "Logged out.",
		"status": 200
		})

@api_view(["POST"])
def log_in(request):
	user = authenticate(
		username=request.data["username"],
		password=request.data["password"]
	)
	if user is not None:
		login(request, user)
		return JsonResponse({
			"message": "user logged in",
			"data": UserSerializer(user).data,
			"status": 200
			})
	else:
		return JsonResponse({
			"message": "Invalid username or password",
			"data": {},
			"status": 401
			})