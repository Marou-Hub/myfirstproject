

from statistics import mean
from random import shuffle

# exemple : Jouer a la maitresse

notes = [
    8, 12, 10,
    9, 4, 20,
    14, 3
]
print(notes)
shuffle(notes)
print(notes)

# module : statistics
result = mean(notes)

print("La moyenne de l'eleve est de {}".format(result))