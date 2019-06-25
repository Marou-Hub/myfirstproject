

# creer une liste qui va stocker des pseudos pour simuler un jeu en ligne
# Graven, Anana, Cleymax ...
online_players = ["Graven", "Anana", "Cleymax", "Bobby"]

print(online_players)

# modifier 'Graven' -> 'Gravenilvec'
online_players [0] = "Gravenilvec"
online_players[2:4] = ["Paul", "Jack"]

# injecter un pseudo a la liste
online_players.insert(2, "BernardGameur123")

# en ajouter d'autres
# on imagine qu'un joueur "Gameur123" se connecte
online_players.append("Gameur123")
online_players.extend(["Gogumer1er", "gigi2k"])

print(online_players)

# le joueur Anana se deconnecte
del online_players[1]
online_players.pop(1)
online_players.remove("gigi2k")

print(online_players)

# si vous souhaitez supprimer tous les elements de votre liste
online_players.clear()

print(online_players)