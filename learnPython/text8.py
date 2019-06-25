
# for : pour une valeur de depart (1), jusqu'à une valeur d'arrivee (5)
for num_client in range(1, 5):
    print("Vous etes le client n°", num_client)

# for each : pour chaque valeur d'une liste données
# lister les emails
emails = ['gravenilvec@gmail.com', 'graven@graven.yt', 'gravendev@yahoo.fr', 'steelaxiss@free.fr', 'contact@graven.yt']

# blacklist
blacklist = ['gravendev@yahoo.fr', 'steelaxiss@free.fr']

# pour chacune des valeurs, j'affiche "Email envoyé à [inserer l'email]
for email in emails:

    if email in blacklist:
        print("Email {} interdit ! Envoi impossible...".format(email))
        continue

    print("Email envoyé à : ", email)

# while : tant qu'une condition est vraie
# salarié 1500€ / mois
salary = 1500

# tant que salaire < 200€, + 120€
while salary < 2000:
    # ajouter 120€ au salaire
    salary += 120
    # afficher le resultat
    print("Votre salaire est actuel est de ", salary, "€")

print("Fin du programme.")

# un youtuber "Gravinou", 2500 abonnés
suscribers_count = 2500

# il gagne 10% d'audience supplémentaire par mois
mounths = 0

# on souhaite estimer combien aura-t-il d'abonnés après 2 ans
while mounths <= 24:
    suscribers_count *= 1.10

    print("Vous avez ectuellement {} abonnés !".format(suscribers_count))
    mounths += 1