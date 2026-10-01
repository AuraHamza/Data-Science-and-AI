import pandas as pd

df=pd.read_csv("Cricketers.csv",index_col="Player")
# print(df)

# Printing every thing in the file 
print(df.to_string())

# printing by column 
print("\nPrinting by column:")
print(df["Role"].to_string())

print("\nPrinting Multiple column:")
print(df[["Country","Role","Rating"]].to_string())

print("\nPrinting Multiple column Using condtion:")
print(df[df["Rating"]>9.5].to_string())
# printing by Row 

print("\nPrinting by row:")
print(df.loc["Rohit Sharma":"Travis Head",["Average","Rating"]])
print("\nInter base Selection")
print(df.iloc[0:11:2].to_string())

# Printing Using Try catch
print("\nPrinting Using Try catch")
Name=input("Enter the player Name:")
try:
    print("\n",df.loc[Name])
except:
    print(Name,"Not Found")