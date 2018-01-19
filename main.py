#!/usr/bin/env python3

import json

def charger_fichier_json(url):
    file = open (url)
    data = json.load(file)

    """Charge le fichier json exercice1.json en mémoire.

    Cette fonction charge la structure de donnée contenue dans un fichier
    json en mémoire et retourne cette structure de données.

    Parameters
    ----------
    nom_fichier : string
        Chemin du fichier à charger en mémoire.

    Returns
    -------
    list | dict
        Structure de données contenant les données du fichier json.
    """
    # Charger les données de nom_fichier dans la variable data

    return data


def afficher_donnees_brutes(data):
    """Affiche les données passées en paramètres en respectant l'ordre des
    lignes et des colonnes.

    Parameters
    ----------
    data : list of string
        Collection contenant les données à afficher.
    """
    for ligne in structure:
        print(ligne)


def afficher_donnees_filtrees(data, chars_to_filter_out=["X"]):
    """Filtre les données passées en paramètre et les affiches
    sans saut de ligne.

    Le passage d’un élément à l’autre dans la liste sera
    interprété comme un espace.

    Parameters
    ----------
    data : list of strings
        Collection contenant les données à afficher.
    chars_to_filter_out : list of strings
        Liste des caractères à éliminer avant affichage
    """
    # pr chaque ligne ds data
    for ligne in data:
        # pr chaque lettre ds la ligne
        for lettre in chars_to_filter_out:
            # si la lettre est ds ma liste à filtrer
            if lettre in chars_to_filter_out=["X"]:
                # je fais rien
                pass
            # sinon
        else:
                # afficher la lettre
                print(lettre)
            # fin si (permet juste de bien visualiser où se termine la condition: ne pas en tenir compte ds le code def)
        # fin pour (permet juste de bien visualiser où se termine la condition: ne pas en tenir compte ds le code def)
        # espace à la fin de la ligne (et non à la fin de chaque lettre)
    # fin pour (permet juste de bien visualiser où se termine la condition: ne pas en tenir compte ds le code def)

# on aurait pu aussi dire
# pr chaque ligne ds data
    # afficher la ligne sans les X (il aurait alors fallu décomposer à nouveau cette ligne: parcourir la ligne lettre par lettre et ignorer les lettres à filtrer)
# fin ligne pour

# NE PAS HESITER À BIEN DÉCOMPOSER LES ÉTAPES

def main():
    """Point d'entrée principal du programme."""
    structure = charger_fichier_json("exercice1.json")
    afficher_donnees_brutes(structure)
    print()# affichage d’un caractère de fin de ligne
    afficher_donnees_filtrees(data)

if __name__ == "__main__":
    main()
