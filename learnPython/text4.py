
# exemple : Systeme de verification de mot de passe
password = input("Entrer votre mot de passe")
password_lenght = len(password)
print(password_lenght)

# verifier si le mot de passe est inferieur a 8 caracteres
if password_lenght <= 8:
    print("Mot de passe trop court !")
elif 8 < password_lenght <= 12:
    print("Mot de passe moyen !")
else:
    print("Mot de passe parfait !")