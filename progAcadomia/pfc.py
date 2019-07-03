
pcf_list = ["pierre", "feuille", "ciseaux"]
from random import shuffle

rep = str(input("Bonjour, voulez-vous jouer avec moi à Pierre/Feuille/Ciseaux ?"))

if rep == "Oui":
    print("Je vais faire le décompte et je répondrai après toi.")
    print("1, 2, 3, pierre, feuille, ciseaux !")
    pcf = input()
    shuffle(pcf_list)
    print(pcf_list[0])
    if pcf == "pierre":
        if pcf_list[0] == "pierre":
            print("C'est un match nul.")
        elif pcf_list[0] == "feuille":
            print("J'ai gagné !")
        else:
            print("J'ai perdu.")
    if pcf == "feuille":
        if pcf_list[0] == "feuille":
            print("C'est un match nul.")
        elif pcf_list[0] == "pierre":
            print("J'ai gagné !")
        else:
            print("J'ai perdu.")
    if pcf == "ciseaux":
        if pcf_list[0] == "ciseaux":
            print("C'est un match nul.")
        elif pcf_list[0] == "feuille":
            print("J'ai gagné !")
        else:
            print("J'ai perdu.")

else:
    print("Dommage... Au-revoir.")
