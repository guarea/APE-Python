#https://pandas.pydata.org/docs/getting_started/intro_tutorials/01_table_oriented.html
import pandas as pd
df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)

print(df["Age"].max())

ages = pd.Series([22, 35, 58], name="Age")
print(ages)
print(ages["Age"])
#print(ages["Age"].max())