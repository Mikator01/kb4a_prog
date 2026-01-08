import csv
import matplotlib.pyplot as plt

furnished = 0
semi_furnished = 0
unfurnished = 0

parking = 0
no_parking = 0

klimatizace = 0
no_klima = 0

boiler = 0
no_boiler = 0

basement = 0
no_basement =0

guestroom = 0
no_guestroom = 0

mainroad = 0
no_mainroad = 0

cesta = r"moje kódy\house-price.csv"
with open(cesta, "r",encoding="utf-8") as file:
    for radek in csv.DictReader(file):
            if(radek["furnishingstatus"]) == "furnished":
                furnished += 1
            elif(radek["furnishingstatus"]) == "semi-furnished":
                semi_furnished += 1
            else:
                unfurnished += 1

            if int(radek["parking"]) >= 1:
                parking += 1
            else:
                no_parking += 1
            
            if(radek["airconditioning"]) == "yes":
                klimatizace += 1
            else:
                no_klima += 1

            if(radek["hotwaterheating"]) == "yes":
                boiler += 1
            else:
                no_boiler += 1

            if(radek["basement"]) == "yes":
                basement += 1
            else:
                no_basement += 1

            if(radek["guestroom"]) == "yes":
                guestroom += 1
            else:
                no_guestroom += 1

            if(radek["mainroad"]) == "yes":
                mainroad += 1
            else:
                no_mainroad += 1
sum (radek("price"))

plt.bar(["Furnished", "Semi-furnished", "Unfurnished"], [furnished, semi_furnished, unfurnished])
plt.show()