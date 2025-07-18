import pandas as pd
df = pd.read_csv("netflix_titles.csv")

print("Count of null entries per column")
print(df.isnull().sum())     # Number of empty values

print("Release year stats")
print(df.describe())         # Basic stats on numeric values

print ("Count of movies vs TV shows")
print(df['type'].value_counts())       # Movies vs TV Shows

print ("Count of rating categories")
print(df['rating'].value_counts())     # Rating categories

print ("Top 10 countries by count of titles")
print(df['country'].value_counts().head(10))  # Top 10 countries

df['date_added'] = pd.to_datetime(df['date_added'])
print("Date range in dataset:")
print(df["date_added"].min(), df['date_added'].max()) #Date range of titles in dataset

print(df['date_added'].dt.year.value_counts().sort_index()) #Distribution of additions by year

print(df['duration'].unique())  #Identification of duration format

df['duration_num'] = df['duration'].str.extract('(\d+)').astype(float) #Extract numbers from string (extract 90 from 90 minutes)

df['duration_type'] = df['duration'].str.extract(r'([a-zA-Z]+)')[0].str.lower().str.strip()  #Catagorize the duration in minutes or seasons by extracting the first alphabetic word. After which, standardizing format

print(df.sample(10).to_string)