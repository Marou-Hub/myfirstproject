
# Place de cinema
# recolter l'age de la personne "Quel est votre age ?"
# si la personne est mineur -> 7€
# si la personne est majeur -> 12€
# souhaitez-vous du pop-corn ?
# si oui -> +5€
# afficher le prix total a payer

age = int(input("Quel est votre age ?"))
if age < 18:
    prix_total = 7
else:
    prix_total = 12

pop_corn_request = input("Voulez-vous du pop-corn ? (Oui, Non)")
if pop_corn_request == "Oui":
    prix_total += 5
    print("Vous devez payer {}€".format(prix_total))
else:
    print("Vous devrez payer {}€".format(prix_total))