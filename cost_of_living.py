import pandas as pd

df = pd.read_csv("COLI_CLEAN.csv")

def get_cost_of_living(state):

    result = df[
        df["GeoName"] == state
    ]

    if result.empty:
        return None

    row = result.iloc[0]

    return float(row["2024"])