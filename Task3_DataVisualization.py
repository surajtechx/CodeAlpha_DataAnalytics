import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("quotes_dataset.csv")
df["Quote_Length"] = df["Quote"].apply(len)

plt.figure(figsize=(10,5))
df["Author"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Authors")
plt.show()

tags = df["Tags"].str.split(", ").explode()
plt.figure(figsize=(10,5))
tags.value_counts().head(10).plot(kind="bar")
plt.title("Top Tags")
plt.show()

sns.histplot(df["Quote_Length"], bins=20)
plt.title("Quote Length Distribution")
plt.show()
