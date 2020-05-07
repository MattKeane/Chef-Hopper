# Chef Hopper
A web scraping app for recipes

## Introduction
Have you ever searched the internet for a recipe and the results turned up a bunch of irrelevant text? Have you ever had a recipe up on your phone while cooking and struggled to read the instructions because the page was too full of ads and decorative elements? Instead of being designed for maximum usability, recipe sites are often designed to maximize ad revenue and search engine optimization. This results in a terrible user experience. Chef Hopper will remedy this by scraping relevant information from popular recipe sites, and returning it in a concise and usy-to-read format.

## User Stories
* The page loads with a simple search bar
* After the user enters their search terms, the page returns a list of results
* Clicking on a result displays a clean and simple version of the recipe
* All elements will be mobile friendly

## Wire Frames
Search bar and results:
![Search bar and results](https://i.imgur.com/l8Gu4IO.png)
Recipe view:
![Recipe view](https://i.imgur.com/uetcgBi.png)

## Data and Database
This project will use MongoDB as its database. When the user enter their search query, the server will first check the database to see if that query has been made before. If not, it will have the scrape the top results from popular recipes sites, save them in the database, and return them to the user. If so, it will pull the saved results from the database and return them to the user, saving a significant amount of time and computational workload.

## Models
![Models](https://i.imgur.com/veBk5ol.png)

## Technologies
* React
* Django
* MongoDB
* BeautifulSoup

## Stretch Goals
* Allow users to toggle between light mode and dark mode
* Allow users to create accounts, upload, edit, and share recipes
* Create a rating system and use that to adjust search results
* Allow users to search by ingredient
* Create a native iOS app with Swift