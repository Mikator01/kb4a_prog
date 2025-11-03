#uloha3

import random

a = random.randint(1, 10)
b = random.randint(1, 10)
operace = random.choice(["+", "-"])

if operace == "+":
    vysledek = a + b
else:
    vysledek = a - b

print("Příklad: ", a, operace, b)
uzivatel_vysledek = int(input("Zadejte výsledek: "))

if uzivatel_vysledek == vysledek:
    print("Správně")
else:
    print("Špatně. Správný výsledek: ", vysledek)