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

def afficher_liste_filtree(data, chars_to_filter_out=["X"]):
    for ligne in data:
        for lettre in ligne:
            if lettre is chars_to_filter_out:
                pass
            else:
                print(lettre, end='')


# aurait-on pu utiliser list.remove?
################################################################################

ligne = data
afficher_liste(ligne)
