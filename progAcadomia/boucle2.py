
max_number = int(input("Combien de personnes êtes-vous ?"))

age_list = []

for number in range(1, max_number+1):
    print("Quel âge a la personne", number, "?")
    age = int(input())
    age_list.append(age)

for number in range(1, max_number+1):
    age = age_list[number-1]
    if age < 14:
        print("La personne", number, "est un enfant.")
    elif 14 < age <= 17:
        print("La personne", number, "est un adolescent.")
    elif 17 < age <= 60:
        print("La personne", number, "est un adulte.")
    else:
        print("La personne", number, "est un senior.")