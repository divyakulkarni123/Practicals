
# Practical 3: Bayesian Network for Heart Disease Diagnosis

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.inference import VariableElimination

# Download and read Heart Disease dataset
cols = ["age", "sex", "cp", "trestbps", "chol", "fbs",
        "restecg", "thalach", "exang", "oldpeak",
        "slope", "ca", "thal", "num"]

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data"

df = pd.read_csv(url, names=cols, na_values="?")

# Prepare data
data = pd.DataFrame()

data["Age"] = df["age"].apply(lambda x: "old" if x > 55 else "young")
data["Chol"] = df["chol"].apply(lambda x: "high" if x > 240 else "normal")
data["MaxHR"] = df["thalach"].apply(lambda x: "low" if x > 150 else "high")
data["HeartDisease"] = df["num"].apply(lambda x: "yes" if x > 0 else "no")

data = data.dropna()

print("Discretised data (first 5 rows):")
print(data.head())

# Create Bayesian Network
model = DiscreteBayesianNetwork([
    ("Age", "HeartDisease"),
    ("Chol", "HeartDisease"),
    ("MaxHR", "HeartDisease")
])

# Train the model
model.fit(data)

# Perform inference
infer = VariableElimination(model)

q1 = infer.query(
    ["HeartDisease"],
    evidence={"Age": "old", "Chol": "high"}
)

q2 = infer.query(
    ["HeartDisease"],
    evidence={"MaxHR": "low"}
)

print("\nP(HeartDisease | Age=old, Chol=high):")
print(q1)

print("\nP(HeartDisease | MaxHR=low):")
print(q2)

# Draw Bayesian Network
G = nx.DiGraph(model.edges())

nx.draw(
    G,
    with_labels=True,
    node_color="lightblue",
    node_size=2500,
    font_size=9,
    arrows=True
)

plt.title("Bayesian Network for Heart Disease")
plt.savefig("lab3_bayesian_network.png", dpi=100)
plt.show()
