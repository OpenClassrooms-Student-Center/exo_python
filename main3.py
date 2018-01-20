data = [
    "XXBXXXiXXeXnXXvXeXXnuXXXXXeXX",
    "XXXXXsXXXXXXuXXXXXXXXXrXXXXXX",
    "OXXXXpeXXnXcXlasXXXsXrXooXmXs",
    "XXXXXXeXXXXXXXtXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXsXXXuXXXXXXrXXX",
    "XXXlXXXXXXXXXXXeXXXXXXXXXXXXX",
    "XXXXXXpXXXXXarXXcXXouXXXrXsXX",
    "XXXDXXXAXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXPXXyXXtXXXhXXXXXoXXXn"
]

def afficher_liste(data):
    i = 0
    while i < len(data):
        print(data[i])
        i += 1
# est ce qu'on aurait pu faire:
        #for elt in data:
        #print(elt) 
            #cette option ne fonctionne pas: pas de message d'erreur ms rien ne s'affiche sur la console
            
    # -tc- La boucle while n'est pas très pythonique. Lorsque c'est possible, on utilise for, comme ci-dessous
    # -tc- for elt in data:
    # -tc-    print(elt)

def afficher_liste_filtree(data, chars_to_filter_out=["X"]):
    for ligne in data:
        for lettre in ligne:
            # -tc- c'est: if lettre is in chars_to_filter_out:
            if lettre is chars_to_filter_out:
                pass
            else:
                print(lettre, end='')
# ne fonctionne pas: pas de message d'erreur, la liste apparait avec les XX


# aurait-on pu utiliser list.remove? -tc- Non, mais ligne.replace('X', '')
################################################################################

ligne = data
afficher_liste(ligne)

print()

# -tc- il faut encore executer afficher_liste_filtrée
afficher_liste_filtree(data)
