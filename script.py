import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}
df = pd.DataFrame(data)
print(df.shape)
print(df.head())
print(df.describe())
print(df.info())
print("Mean of all age :",df["Age"].mean())