import os
# attention chemin à adapter à votre ordinateur!
chemin = r"C:\Users\ilyas\pythonCode\bts\chp9\monDossier\korri.txt"

saisie = ""
while not saisie == "q":
    with open(chemin ,"a") as f:
        saisie = input("\nSaisir :> ")
        contenu = f.write(saisie + "\n")


    with open(chemin ,"r") as f:
        contenu = f.read()
        print(contenu)
os.startfile(r"C:\Users\ilyas\pythonCode\bts\chp9\monDossier\korri.txt")
    