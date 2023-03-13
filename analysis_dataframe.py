import pandas as pd
df = pd.read_csv("data/airport.csv")
# print(df)
# print(df.head(5)) #top 5 rows
# print(df.tail(4)) #last 4 rows
print(df.info())
print(df.describe())