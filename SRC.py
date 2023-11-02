# Main.py
import tkinter as tk
import csv
import random
from tkinter import Toplevel, Message

class Application(tk.Tk):

    def __init__(self):
        super().__init__()

        self.recipes_desserts = self.load_data("/home/spooke/Documents/Projet_Cuisine_Aleatoire/Recettes_Desserts.csv")
        self.recipes_entrees = self.load_data("/home/spooke/Documents/Projet_Cuisine_Aleatoire/Recettes_Entré.csv")
        self.recipes_poissons = self.load_data("/home/spooke/Documents/Projet_Cuisine_Aleatoire/Recettes_Poissons.csv")
        self.recipes_viandes = self.load_data("/home/spooke/Documents/Projet_Cuisine_Aleatoire/Recettes_Viandes.csv")


        self.title("SRC")
        self.configure(bg="#3d3d5c")
        self.geometry("400x600")

        tk.Label(self, text="Spooke_Retro_Cooking", bg="#3d3d5c", fg="white", font=("Fantasy", 20, "bold")).pack(pady=20)

        # Icônes pour les boutons (assurez-vous que les chemins sont corrects)
        self.icon_pieapple = tk.PhotoImage(file="/home/spooke/Documents/Projet_Cuisine_Aleatoire/Food_Pictures_Assets/PieApple.png")
        self.icon_olive = tk.PhotoImage(file="/home/spooke/Documents/Projet_Cuisine_Aleatoire/Food_Pictures_Assets/Olive.png")
        self.icon_boar = tk.PhotoImage(file="/home/spooke/Documents/Projet_Cuisine_Aleatoire/Food_Pictures_Assets/Boar.png")
        self.icon_fish = tk.PhotoImage(file="/home/spooke/Documents/Projet_Cuisine_Aleatoire/Food_Pictures_Assets/Fish.png")
        self.icon_whiskey = tk.PhotoImage(file="/home/spooke/Documents/Projet_Cuisine_Aleatoire/Food_Pictures_Assets/Whiskey.png")

        # Boutons pour chaque catégorie de recette
        self.create_button("Dessert", self.icon_pieapple, self.afficher_dessert).pack(fill=tk.X, padx=30, pady=10)
        self.create_button("Salade", self.icon_olive, self.afficher_salade).pack(fill=tk.X, padx=30, pady=10)
        self.create_button("Viande", self.icon_boar, self.afficher_viande).pack(fill=tk.X, padx=30, pady=10)
        self.create_button("Poisson", self.icon_fish, self.afficher_poisson).pack(fill=tk.X, padx=30, pady=10)
        self.create_button("Recette aléatoire", self.icon_whiskey, self.recette_aleatoire).pack(fill=tk.X, padx=30, pady=20)

    def create_button(self, text, icon, command):
        return tk.Button(self, text=text, image=icon, compound=tk.LEFT, bg="#FFA500", fg="black", font=("Fantasy", 16), command=command)

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

    def show_recipe_window(self, recipe, category):
        new_window = Toplevel(self)
        new_window.title(f"Recette de {category.capitalize()}")
        new_window.configure(bg="#3d3d5c")
        new_window.geometry("400x600")

        label_title = tk.Label(new_window, text=recipe["title"], bg="#3d3d5c", fg="white", font=("Helvetica", 20, "bold"))
        label_title.pack(pady=20)

        label_ingredients = tk.Label(new_window, text="\n".join(recipe["ingredients"]), bg="#3d3d5c", fg="white", justify=tk.LEFT, font=("Helvetica", 14))
        label_ingredients.pack(pady=20)
        label_ingredients.bind("<Configure>", lambda e: label_ingredients.config(wraplength=new_window.winfo_width() - 20))

    def display_recipe(self, category):
        recipes_list = self.recipes_desserts + self.recipes_entrees + self.recipes_poissons + self.recipes_viandes
        if category != "aleatoire":
            category_map = {
                "dessert": self.recipes_desserts,
                "entree": self.recipes_entrees,
                "poisson": self.recipes_poissons,
                "viande": self.recipes_viandes
            }
            recipes_list = category_map[category]
        
        recipe = random.choice(recipes_list)
        self.show_recipe_window(recipe, category)

    def afficher_dessert(self):
        self.display_recipe("dessert")

    def afficher_salade(self):
        self.display_recipe("entree")

    def afficher_viande(self):
        self.display_recipe("viande")

    def afficher_poisson(self):
        self.display_recipe("poisson")

    def recette_aleatoire(self):
        self.display_recipe("aleatoire")

if __name__ == "__main__":
    app = Application()
    app.mainloop()
