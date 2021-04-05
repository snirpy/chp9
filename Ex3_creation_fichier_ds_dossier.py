import os
from datetime import datetime

heure_actuelle = datetime.now()

#chemin du dossier de travail
# chemin = r"C:\Users\Lenovo\codage\json\creation_et_saisie_fichier"

chemin= os.getcwd() # permet de récupérer le chemin du dossier courant
print("le chemin courant est: ",chemin)

#concaténation nom du sous dossier avec le dossier parent
chemin_dossier= os.path.join(chemin,"monDossier")
#création du sossier s'il n'existe pas
if not os.path.exists(chemin_dossier):
    os.makedirs(chemin_dossier)
    print("Le dossier 'monDossier' a été créé")
else:
    print("Le dossier 'monDossier' existe déja!")
 
#création du fichier s'il n'existe pas et afficher l'heure de création
if not os.path.isfile('Bilan_TP_Python.txt'):
    with open(chemin_dossier+'/Bilan_TP_Python.txt','a') as f:
        contenu = f.write(f"dossier créé {heure_actuelle}\n")
        print("Création du fichier")
else:
    print("Le fichier existe déja!")



chemin_fichier = chemin_dossier+'\\Bilan_TP_Python.txt'
print("Création du chemin de fichier :",chemin_fichier)

# chemin_fichier = r"C:\Users\Lenovo\codage\python_code_bts\python_bts-snir1\hello.txt"
saisie = ""
while not saisie == "q":
    with open(chemin_fichier ,"a") as f:
        saisie = input("\nSaisir :> ")
        contenu = f.write(saisie + "\n")


    with open(chemin_fichier ,"r") as f:
        # saisie = input("\nSaisir :> ")
        contenu = f.read()
        print(contenu)
    
