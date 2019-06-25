
from random import shuffle

# generateur de phrases
# demander en console une chaine de la forme "mot1/mot2/mot3/mot4/..."
chained_words = input("Entrer une chaine de la forme mot1/mot2/mot3/mot4")

# transformer cette chaine en une liste
words = chained_words.split("/")

# la melanger
shuffle(words)
print(words)

# recuperer le nombre d'elements
words_len = len(words)

# si le nombre d'element de cette liste est inferieur a 10
if words_len < 5:
    # -> afficher les deux premiers mots
    print(words[0:2])

# si le nombre d'elements est superieur a 10
else:
    # -> afficher les trois derniers mots
    print(words[- 1], words[words_len - 2], words[words_len - 3])