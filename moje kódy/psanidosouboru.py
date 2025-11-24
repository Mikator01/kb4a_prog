#1

import random

def generuj_cisla(min_val, max_val, pocet):
    return [random.randint(min_val, max_val) for _ in range(pocet)]

cisla = generuj_cisla(1, 100, 20)
print(cisla)

cesta = "moje kódy/cisla.txt"

with open(cesta, "w", encoding="utf-8") as soubor:
    for cislo in cisla:
        soubor.write(str(cislo)+"\n")

#2

import random

soubor = "moje kódy\chatlog.txt"

print("Textový chat. Napiš 'konec' jako zprávu pro ukončení.\n")

while True:
    uzivatel = input("Zadej uživatelské jméno: ")
    zprava = input("Zadej zprávu: ")

    if zprava.lower() == "konec":
        print("Chat ukončen.")
        break

    with open(soubor, "a", encoding="utf-8") as file:
        file.write(uzivatel, zprava + "\n")

    print("Zpráva uložena s ID")