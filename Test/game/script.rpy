# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# # Déclarez les personnages utilisés dans le jeu.
# define e = Character('Eileen', color="#c8ffc8")


# # Le jeu commence ici
# label start:

#     e "Vous venez de créer un nouveau jeu Ren'Py."

#     e "Après avoir ajouté une histoire, des images et de la musique, vous pourrez le présenter au monde entier !"

#     return

# Définition des personnages

    

# Définition des décors
image salle_a_manger = "chaise-nordique-et-table-en-bois-dans-salle-a-manger-scandinave.jpeg"
image chambre = "decoration-chambre-a-coucher-sobre.jpeg"
image salle_de_bain = "istockphoto-1308282338-612x612.jpg"

# Utilisation des images dans les scènes
label start:
    scene chambre
    show logo
    "Bienvenue dans la chambre !"
    "..."
    "Que veux-tu faire ?"

    menu:
        "Aller dans la salle de bain":
            jump salle_de_bain_scene
        "Aller dans la salle à manger":
            jump salle_a_manger_scene

label salle_de_bain_scene:
    scene salle_de_bain
    show logo
    "Vous êtes dans la salle de bain."
    "Que souhaitez-vous faire ensuite ?"

    menu:
        "Aller dans la chambre":
            jump start
        "Aller dans la salle à manger":
            jump salle_a_manger_scene
        "Sortir de la maison":
            "Fin du jeu."
            return

label salle_a_manger_scene:
    scene salle_a_manger
    show logo
    "Vous êtes dans la salle à manger."
    "Que souhaitez-vous faire ensuite ?"

    menu:
        "Aller dans la chambre":
            jump start
        "Aller dans la salle de bain":
            jump salle_de_bain_scene
        "Sortir de la maison":
            "Fin du jeu."
            return
