
# code
wallet = 5000
computer_price = 50000

# le prix de l'ordinateur est inferieur a 1000€
if computer_price <= wallet or computer_price > 1000:
    print("L'achat est possible")
    wallet -= computer_price
else:
    print("L'achat est impossible, vous n'avez que {}€".format(wallet))

print(wallet)