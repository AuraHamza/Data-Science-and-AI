import pandas as pd 

df=pd.read_csv("Cricketers.csv")

# whole dataframe 
# print("\nMean of the Data")
# print(df.mean(numeric_only=True))
# print("\nSum of the Data")
# print(df.sum(numeric_only=True))
# print("\nMax of the Data")
# print(df.max(numeric_only=True))
# print("\nMin of the Data")
# print(df.min(numeric_only=True))
# print("\nCount of the Data")
# print(df.count())

# Single DataSet
# print("\nMean of the Data")
# print(df["Average"].mean())
# print("\nSum of the Data")
# print(df["Average"].sum())
# print("\nMax of the Data")
# print(df["StrikeRate"].max())
# print("\nMin of the Data")
# print(df["StrikeRate"].min())
# print("\nCount of the Data")
# print(df["Average"].count())


print("\n Group-BY ")

group=df.groupby("Country")

print(group["Average"].mean())