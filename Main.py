# Main.py
import tkinter as tk
from tkinter import messagebox
import csv
import random

class Application(tk.Tk):

    def __init__(self):
        super().__init__()

        # Charger les données depuis les fichiers CSV
        self.recipes_desserts = self.load_data("Recettes_Desserts.csv")
        self.recipes_entrees = self.load_data("Recettes_Entré.csv")
        self.recipes_poissons = self.load_data("Recettes_Poissons.csv")
        self.recipes_viandes = self.load_data("Recettes_Viandes.csv")

        # Configuration générale de la fenêtre
        self.title("Application de Cuisine")
        self.configure(bg="#1a1a2e")  # fond bleu foncé
        self.geometry("400x600")  # Format smartphone (ajustez selon vos préférences)

        # Ajout d'un titre
        tk.Label(self, text="Application de Cuisine", bg="#1a1a2e", fg="white", font=("Arial", 20, "bold")).pack(pady=20)

        # Boutons de classification
        self.create_button("Dessert", self.afficher_dessert).pack(fill=tk.X, padx=30, pady=10)
        self.create_button("Salade", self.afficher_salade).pack(fill=tk.X, padx=30, pady=10)
        self.create_button("Viande", self.afficher_viande).pack(fill=tk.X, padx=30, pady=10)
        self.create_button("Poisson", self.afficher_poisson).pack(fill=tk.X, padx=30, pady=10)
        self.create_button("Recette aléatoire", self.recette_aleatoire).pack(fill=tk.X, padx=30, pady=20)

    def create_button(self, text, command):
        return tk.Button(self, text=text, bg="#FFA500", fg="black", font=("Arial", 16), command=command)

    def load_data(self, file_name):
        recipes = []
        with open(file_name, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)  # skip header row
            for row in reader:
                recipes.append({
                    "title": row[0],
                    "ingredients": row[1].split(", "),
                    # "instructions": row[2]  # Si vous ajoutez des instructions plus tard
                })
        return recipes

    def format_recipe_info(self, recipe):
        title = recipe["title"]
        ingredients_text = "\n".join(recipe["ingredients"])
        return f"{title}\n\nIngrédients:\n{ingredients_text}"

    def display_recipe(self, category):
        if category == "dessert":
            recipes_list = self.recipes_desserts
        elif category == "entree":
            recipes_list = self.recipes_entrees
        elif category == "poisson":
            recipes_list = self.recipes_poissons
        elif category == "viande":
            recipes_list = self.recipes_viandes
        else:  # random
            recipes_list = self.recipes_desserts + self.recipes_entrees + self.recipes_poissons + self.recipes_viandes
        
        recipe = random.choice(recipes_list)
        info = self.format_recipe_info(recipe)
        messagebox.showinfo(f"Recette {category.capitalize()}", info)

    # Changez vos fonctions pour utiliser la nouvelle méthode display_recipe
    def afficher_dessert(self):
        self.display_recipe("dessert")

    def afficher_salade(self):
        self.display_recipe("entree")

    def afficher_viande(self):
        self.display_recipe("viande")

    def afficher_poisson(self):
        self.display_recipe("poisson")

    def recette_aleatoire(self):
        self.display_recipe("random")

if __name__ == "__main__":
    app = Application()
    app.mainloop()
