import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def train_model(data):
    df = pd.DataFrame(data)
    X = df[["experience", "rating"]]
    y = df["popularity"]

    model = RandomForestClassifier()
    model.fit(X, y)

    return model