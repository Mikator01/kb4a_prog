import matplotlib.pyplot as plt
import csv
import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix

# ---------- Načtení CSV pomocí Pandas a úprava dat ----------
data = pd.read_csv(r"3. strojove_uceni\data\titanic.csv")

X = []  # = vstupy
Y = []  # = výstupy


for _, row in data.iterrows():  # Používáme Pandas iterrows pro procházení řádků
    age = float(row["Age"])
    pclass = float(row["Pclass"])
    surv = float(row["Survived"])

    if row["Sex"] == "male":
        sex = 0
    else:
        sex = 1

    X.append([sex, age, pclass])
    Y.append(surv)

# ---------- Ruční rozdělení na trénování a testování ----------
rows = len(X)
split = round(0.8 * rows)

trening_X = X[:split]
trening_Y = Y[:split]

test_X = X[split:]
test_Y = Y[split:]

# ---------- Neuronová síť ----------
neural_network = MLPClassifier(
    hidden_layer_sizes=(10, 10),
    random_state=4
)

neural_network.fit(trening_X, trening_Y)


# ---------- Vyhodnocení ----------
results = neural_network.predict(test_X)

correct = 0
for i in range(len(results)):
    if test_Y[i] == results[i]:
        correct += 1
print(correct / len(results))

print(confusion_matrix(test_Y, results))