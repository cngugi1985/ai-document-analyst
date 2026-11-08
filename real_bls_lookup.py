import pandas as pd

df = pd.read_csv(
    "wagedex-state-wages.csv",
    comment="#"
)


def get_real_compensation(
    occupation,
    state
):
    result = df[
        (df["occ_title"] == occupation)
        &
        (df["state"] == state)
    ]

    if result.empty:
        return None

    row = result.iloc[0]

    return {
        "occupation": row["occ_title"],
        "state": row["state"],
        "median_wage": row["median_annual_wage"]
    }