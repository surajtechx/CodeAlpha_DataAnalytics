import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("quotes_dataset.csv")

print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
print("Duplicates:", df.duplicated().sum())

df["Quote_Length"] = df["Quote"].apply(len)

df["Author"].value_counts().head(10).plot(kind="bar")
plt.title("Top Authors")
plt.show()

df["Quote_Length"].plot(kind="hist", bins=20)
plt.title("Quote Length Distribution")
plt.show()
