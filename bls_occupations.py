import pandas as pd

df = pd.read_csv(
    "wagedex-state-wages.csv",
    comment="#"
)

def get_all_occupations():

    return sorted(
        df["occ_title"]
        .dropna()
        .unique()
        .tolist()
    )