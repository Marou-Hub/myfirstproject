
def main():
    # recolter une valeur porte monnaie
    wallet = int(input("Entrer la valeur dans le porte monnaie"))
    print("Vous avez actuellement ", wallet, " euros.")
    # creer un produit qui aura pour valeur 50
    produit = 50
    print("Le produit vaut ", produit, " euros.")
    # afficher la nouvelle valeur du porte monnaie, apres son achat
    wallet = wallet - produit
    print("Il vous reste ", wallet, "euros.")


main()
