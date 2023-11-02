# Projet-SRC



Chargement des Données :

    Au démarrage, l'application charge des données depuis des fichiers CSV. Chaque fichier correspond à une catégorie de recettes (desserts, entrées, poissons, viandes).
    Ces fichiers contiennent les titres des recettes et leurs ingrédients.




Affichage des Recettes :

    Lorsqu'un utilisateur clique sur un bouton, l'application sélectionne aléatoirement une recette dans la catégorie correspondante.
    Une nouvelle fenêtre s'ouvre alors, affichant le titre de la recette et la liste des ingrédients.
    La mise en page de la fenêtre de recette s'adapte à la taille de celle-ci, assurant que le texte reste lisible peu importe la taille de la fenêtre.




 Fonctionnement Interne :

    L'application utilise le module tkinter de Python pour créer l'interface graphique.
    Des fonctions internes sont dédiées au chargement des données, à la création de l'interface utilisateur et à l'affichage des recettes.
    La sélection aléatoire des recettes est rendue possible grâce à l'utilisation du module random.

Extensibilité :

    Le code est structuré de manière à faciliter l'ajout de nouvelles catégories ou recettes simplement en mettant à jour les fichiers CSV.
