from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User

class Recipe(models.Model):
	url = models.CharField(max_length=511)
	title = models.CharField(max_length=255)
	ingredients = ArrayField(
		models.CharField(max_length=255))
	instructions = ArrayField(
		models.TextField())
	avg_rating = models.FloatField(default=0)

class Search(models.Model):
	search_term = models.CharField(max_length=128)
	recipe = models.ForeignKey("Recipe", on_delete=models.CASCADE)

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	saved_recipe = models.ManyToManyField(Recipe)