import pandas as pd

df = pd.read_csv(
    "wagedex-state-wages.csv",
    comment="#"
)

matches = df[
    df["occ_title"].str.contains(
        "Industrial Engineers",
        case=False,
        na=False
    )
]

print(
    matches[
        [
            "occ_title",
            "state",
            "median_annual_wage"
        ]
    ]
    .head(1)
    .to_string()
)