import pandas as pd
df = pd.read_csv("netflix_titles.csv")
#print (df.head())
#print(list(df.info()))
print(df.isnull().sum())
print(df.describe())