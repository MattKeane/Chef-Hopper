from django.db import models
from django.contrib.postgres.fields import ArrayField
from rest_framework import serializers

class Recipe(models.Model):
	url = models.CharField(max_length=511)
	title = models.CharField(max_length=255)
	ingredients = ArrayField(
		models.CharField(max_length=255))
	instructions = ArrayField(
		models.CharField(max_length=255))

class Search(models.Model):
	search_term = models.CharField(max_length=128)
	recipe = models.ForeignKey("Recipe", on_delete=models.CASCADE)