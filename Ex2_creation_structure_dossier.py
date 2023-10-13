import os

# attention chemin à adapter à votre ordinateur!
chemin = r"/Users/ikorri/codage/python/python2023Exos"

liste_dossier  = ["C++", "Python","Javascript"]

for element in liste_dossier:
    chemin_dossier = os.path.join(chemin, "monDossier", element )
    if not os.path.exists(chemin_dossier):
        os.makedirs(chemin_dossier)
        print("Le dossier",element,"a été créé")
    else:
        print("Le dossier",element,"existe déja")
