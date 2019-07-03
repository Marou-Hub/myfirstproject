
number = int(input("Combien de personnes êtes-vous ?"))

for number in range(1, number+1):
    print("Quel âge a la personne", number, "?")
    age = int(input())
    if age < 14:
        print("Tu es un enfant.")
    elif 14 < age <= 17:
        print("Tu es un adolescent.")
    elif 17 < age <= 60:
        print("Tu es un adulte.")
    else:
        print("Tu es un senior.")