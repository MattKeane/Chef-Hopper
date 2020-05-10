from bs4 import BeautifulSoup
import requests
import time

def get_all_recipes_urls(query):
	search_url = "https://www.allrecipes.com/search/results"
	payload = {"wt": query}
	search_response = requests.get(search_url, payload)
	search_soup = BeautifulSoup(search_response.text)
	recipe_urls = search_soup.find_all("div", class_="fixed-recipe-card__info")
	recipe_urls = [url.find("a")["href"] for url in recipe_urls]
	return recipe_urls

def scrape_all_recipes_recipe(url):
	response = requests.get(url)
	soup = BeautifulSoup(response.text)
	try:
		soup.find("body")["class"]
		title = str(soup.find("h1", class_="headline").string)
		ingredients = soup.find_all("span", class_="ingredients-item-name")
		ingredients = [str(ingredient.string).strip() for ingredient in ingredients]
		instruction_section = soup.find("ul", class_="instructions-section")
		instructions = [str(p.string) for p in instruction_section.find_all("p")]
	except KeyError:
		title = str(soup.find("h1", id="recipe-main-content").string)
		ingredients = soup.find_all("span", itemprop="recipeIngredient")
		ingredients = [str(ingredient.string).strip() for ingredient in ingredients]
		instructions = soup.find_all("span", class_="recipe-directions__list--item")
		instructions = [str(instruction.string) for instruction in instructions if instruction.string]
	finally:
		return {
			"url": url,
			"title": title,
			"ingredients": ingredients,
			"instructions": instructions,
		}


def scrape_recipes(query, recipes_per_site):
	urls = get_all_recipes_urls(query)[:recipes_per_site]
	recipes = []
	for url in urls:
		time.sleep(1)
		recipes.append(scrape_all_recipes_recipe(url))
	return recipes


