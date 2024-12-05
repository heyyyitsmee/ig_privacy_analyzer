import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
import pickle

data = np.array([
    [1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 1, 0, 0, 1]
    ])

y = np.array(["Low Risk", "Moderate Risk", "High Risk", "Moderate Risk", "High Risk"])
model = DecisionTreeClassifier()
model.fit(data, y)

with open("privacy_model.pkl", "wb") as file:
    pickle.dump(model, file)
