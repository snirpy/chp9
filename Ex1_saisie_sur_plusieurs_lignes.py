import os
# import subprocess

# Attention : adaptez le chemin à votre ordinateur
chemin = r"/Users/ikorri/codage/python/python2023Exos/korri.txt"

saisie = ""
while saisie.lower() != "q":
    saisie = input("\nSaisir :> ")
    if saisie.lower() != "q":
        with open(chemin, "a") as f:
            f.write(saisie + "\n")

    with open(chemin, "r") as f:
        contenu = f.read()
        print(contenu)
# os.startfile(r"/Users/ikorri/codage/python/python2023Exos/korri.txt")
# subprocess.run(["open", chemin])
    
