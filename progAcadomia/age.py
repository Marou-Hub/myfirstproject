
age = int(input("Quel âge as-tu ?"))

if age < 14:
    print("Tu es un enfant.")
elif 14 < age <= 17:
    print("Tu es un adolescent.")
elif 17 < age <= 60:
    print("Tu es un adulte.")
else:
    print("Tu es un senior.")

