from bs4 import BeautifulSoup
import requests

def get_all_recipes_urls(query):
	search_url = "https://www.allrecipes.com/search/results"
	payload = {"wt": query}
	search_response = requests.get(search_url, payload)
	search_soup = BeautifulSoup(search_response.text)
	recipe_urls = search_soup.find_all("div", class_="fixed-recipe-card__info")
	recipe_urls = [url.find("a")["href"] for url in recipe_urls]
	return recipe_urls