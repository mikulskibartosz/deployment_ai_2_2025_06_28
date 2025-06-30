import json
import pandas as pd

URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/titanic.csv"
df = pd.read_csv(URL)

print(df.head())

summary = {
    "sex": df["sex"].value_counts().to_dict(),
    "survived": {
        "alive": int(df["survived"].sum()),
        "dead": int((df["survived"] == 0).sum())
    }
}

print("\nSummary:")
print(summary)

with open("summary.json", "w") as f:
    json.dump(summary, f)
