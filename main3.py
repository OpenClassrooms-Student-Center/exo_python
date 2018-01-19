def afficher_donnees_filtrees(data, chars_to_filter_out=["X"]):
    for ligne in data:
        for lettre in chars_to_filter_out:
            if lettre is chars_to_filter_out:
                pass
            else:
                print(lettre)

afficher_donnees_filtrees(lettre)
