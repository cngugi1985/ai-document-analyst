import pandas as pd

df = pd.read_csv(
    "wagedex-state-wages.csv",
    comment="#"
)

# normalize columns once
df["occ_title"] = df["occ_title"].astype(str).str.strip()
df["state"] = df["state"].astype(str).str.strip()


def get_real_compensation(
    occupation,
    state
):
    occupation = str(occupation).strip()
    state = str(state).strip()

    result = df[
        (df["occ_title"].str.lower() == occupation.lower())
        &
        (df["state"].str.lower() == state.lower())
    ]

    if result.empty:
        return None

    row = result.iloc[0]

    return {
        "occupation": row["occ_title"],
        "state": row["state"],
        "median_wage": row["median_annual_wage"]
    }