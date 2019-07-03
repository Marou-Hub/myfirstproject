
word_list = ["t", "e", "s", "t"]
answer_list = ["_", "_", "_", "_"]
chance = 10

rep = str(input("Bonjour, voulez-vous jouer avec moi au pendu ?"))

if rep == "Oui":
    print("Mon mot comporte 4 lettres.")

    while answer_list != word_list and chance > 0:
        print("Donne-moi une lettre.")
        letter = input()
        if letter == "t":
            answer_list[0] = "t"
            answer_list[3] = "t"
            print(answer_list)
        elif letter == "e":
            answer_list[1] = "e"
            print(answer_list)
        elif letter == "s":
            answer_list[2] = "s"
            print(answer_list)
        else:
            print("Faux.")
            chance -= 1
            print("Il te reste {} chance(s).".format(chance))
            if chance == 0:
                print("Tu as perdu.")

    if answer_list == word_list:
        print("Tu as gagné !")

else:
    print("Dommage... Au-revoir.")