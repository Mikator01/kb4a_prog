import csv
import matplotlib.pyplot as plt

pocet_male = 0
pocet_female = 0
pocet_umrti = 0
pocet_prezivsi = 0

cesta = r"2. prace_se_soubory\data\titanic.csv"
with open(cesta, "r",encoding="utf-8") as file:
    for radek in csv.DictReader(file):
        if(radek["Sex"]) == "female":
            pocet_female += 1
        else:
            pocet_male += 1

        if int(radek["Survived"]) >= 1:
            pocet_prezivsi += 1
        else:
            pocet_umrti += 1

print("pocet zen: ", pocet_female)
print("pocet muzu: ", pocet_male)
print("pocet umrti: ", pocet_umrti)
print("pocet prezivsich: ", pocet_prezivsi)

plt.bar(["Muži", "Ženy"], [pocet_male, pocet_female])
plt.show