import csv

from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay

X = []  # vstupy
Y = []  # výstupy

with open("moje kódy\data.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["Calories"] == "":
            continue
        duration = float(row["Duration"])
        pulse = float(row["Pulse"])
        maxpulse = float(row["Maxpulse"])
        calories = float(row["Calories"])

        #kategorie z calories
        if calories < 240:
            category = 0
        elif calories < 350:
            category = 1
        else:
            category = 2

        X.append([duration, pulse, maxpulse])
        Y.append(category)

trening_X, test_X, trening_Y, test_Y  = train_test_split(
        X, Y,
        test_size=0.2,
        random_state=42)

neural_network = MLPClassifier(
    hidden_layer_sizes=(22, 8),
    activation="relu",
    max_iter=3500,
    verbose = True,
    random_state=4,
    n_iter_no_change=20
)

neural_network.fit(trening_X, trening_Y)

results = neural_network.predict(test_X)

correct = 0
for i in range(len(results)):
    if test_Y[i] == results[i]:
        correct += 1
print("Přesnost:", correct / len(results))

ConfusionMatrixDisplay.from_predictions(
    test_Y, results)
plt.show()