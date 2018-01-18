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

    structure = charger_fichier_json('exercice1.json')

    print(structure[1])


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
    pass

def main():
    """Point d'entrée principal du programme."""
    structure = charger_fichier_json("exercice1.json")
    afficher_donnees_brutes(data)
    print()# affichage d’un caractère de fin de ligne
    afficher_donnees_filtrees(data)

if __name__ == "__main__":
    main()
