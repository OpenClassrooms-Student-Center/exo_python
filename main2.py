import json

# Entrée : url du fichier à charger (chaine de caractères)
# Sortie : data = fichier.json chargé (liste)
def charger_fichier_json(url):
    file = open (url)
    data = json.load(file)
    return data

# Entrée : data (liste) = la liste à afficher ligne par ligne
def afficher_donnees_brutes(data):
    for ligne in data:
        print(ligne)


######################################################


structure = charger_fichier_json('exercice1.json')
afficher_donnees_brutes(structure)
