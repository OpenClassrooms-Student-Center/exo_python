import json

# Entrée : url du fichier à charger (chaine de caractères)
# Sortie : data = fichier.json chargé (liste)
def charger_fichier_json(url):
    json_file = open (url)
    data = json.load(json_file)
    return data

# Entrée : data (liste) = la liste à afficher ligne par ligne
def afficher_donnees_brutes(data):
    for ligne in data:
        print(ligne)

def afficher_donnees_filtrees(data, chars_to_filter_out=["X"]):
    data = json.load(json_file)
    for ligne in data:
        for lettre in chars_to_filter_out:
            if lettre is chars_to_filter_out:
                pass
            else:
                print(lettre)



######################################################


structure = charger_fichier_json('exercice1.json')
afficher_donnees_brutes(structure)
afficher_donnees_filtrees(data)
