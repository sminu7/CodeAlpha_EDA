

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


sns.set(style="whitegrid")


df = pd.read_csv("netflix_titles.csv")

print("\n🔹 Dataset Shape:", df.shape)
print("\n🔹 Dataset Columns:", df.columns.tolist())
print("\n🔹 Missing Values:\n", df.isnull().sum())


df['date_added'] = df['date_added'].astype(str).str.strip()

df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')


print("\n🔹 Dataset Info:")
print(df.info())
print("\n🔹 Descriptive Statistics (numeric):\n", df.describe())

plt.figure(figsize=(6,4))
sns.countplot(x="type", data=df, palette="viridis")
plt.title("Movies vs TV Shows on Netflix")
plt.show()


plt.figure(figsize=(10,5))
sns.histplot(df['release_year'], bins=40, kde=False, color="red")
plt.title("Content Released per Year")
plt.show()


plt.figure(figsize=(10,5))
df['country'].value_counts().head(10).plot(kind="bar", color="skyblue")
plt.title("Top 10 Countries with Netflix Content")
plt.ylabel("Count")
plt.show()


plt.figure(figsize=(8,4))
sns.countplot(y="rating", data=df, order=df['rating'].value_counts().index, palette="coolwarm")
plt.title("Distribution of Content Ratings")
plt.show()


plt.figure(figsize=(12,6))
df['year_added'] = df['date_added'].dt.year
df['year_added'].value_counts().sort_index().plot(kind="line", marker="o")
plt.title("Content Added to Netflix Over Time")
plt.xlabel("Year Added")
plt.ylabel("Number of Titles")
plt.show()
