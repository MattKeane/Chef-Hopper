from django.db import models
from django.contrib.postgres.fields import ArrayField

class Recipe(models.Model):
	url = models.CharField(max_length=2048),
	title = models.CharField(max_length=256),
	ingredients = ArrayField(
		models.CharField(max_length=256))
	instructions = ArrayField(
		models.CharField(max_length=256))

class Search(models.Model):
	search_term = models.CharField(max_length=128)
	recipe = models.ForeignKey("Recipe", on_delete=models.CASCADE)

# Create your models here.
