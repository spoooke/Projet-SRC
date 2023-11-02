import requests
from bs4 import BeautifulSoup
import csv

def extract_recipe_details(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract ingredients
    ingredient_tags = soup.select(".ingredient_label")
    ingredient_qte_tags = soup.select(".ingredient_qte")
    ingredients = [f"{ingredient.get_text(strip=True)} ({ingredient_qte_tags[i].get_text(strip=True)})" for i, ingredient in enumerate(ingredient_tags)]

    return ingredients

def save_to_csv(title, ingredients):
    with open("recipes.csv", mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([title, ", ".join(ingredients), ""])  # Assuming instructions are still empty for now

def scrape_category_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all recipe titles and URLs on the category page
    recipe_links = soup.select(".tile_title")
    for link in recipe_links:
        title = link.get_text(strip=True)
        full_url = "https://www.cuisineaz.com" + link['href']
        ingredients = extract_recipe_details(full_url)
        save_to_csv(title, ingredients)

# Create a new CSV with headers
with open("recipes.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Titre", "Ingrédients", "Instructions"])

# Scrape the category page
scrape_category_page("https://www.cuisineaz.com/categories/entrees-cat48785")
