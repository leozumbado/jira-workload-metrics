import pandas as pd

def load_dataset(path):
    df = pd.read_csv(path)

    df["Due date"] = pd.to_datetime(df["Due date"])
    df["Updated date"] = pd.to_datetime(df["Updated date"])

    return df