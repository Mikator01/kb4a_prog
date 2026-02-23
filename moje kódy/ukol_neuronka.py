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
        if calories < 350:
            category = 0
        elif calories < 450:
            category = 1
        else:
            category = 2

        X.append([duration, pulse, maxpulse])
        Y.append(category)

rows = len(X)
split = round(0.8 * rows)

trening_X = X[:split]
trening_Y = Y[:split]

test_X = X[split:]
test_Y = Y[split:]

neural_network = MLPClassifier(
    hidden_layer_sizes=(8, 4),
    activation="relu",
    max_iter=2000,
    verbose = True,
    random_state=4
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