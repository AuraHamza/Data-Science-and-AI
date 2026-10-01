import pandas as pd

data={
    "Name":["Falak","Nocki","IQ","Huziafa","T24"],
    "Age":[20 , 26 , 22 , 23 , 21]
}
df=pd.DataFrame(data,index=["Player1","Player2","Player3","Player4","Player5"])
print(df)

print("\nUsing Loc")
print(df.loc["Player1"])

print("\nUsing Iloc")
print(df.iloc[1,0])

# Adding a new column 
df ["Role"] = ["Assaulter","Scouter","IGL","Fragger","Support-Player"]
print("\nAdding new Column:")
print(df)

# Adding new row 
new_row=pd.DataFrame([{"Name":"Shaheen","Age":32,"Role":"Analysit"}],index=["Coach"])
df = pd.concat([df,new_row])
print("\nAdding new Row:")
print(df)

# Adding Multiple Columns
df[["Country","Kills"]]=[
    ["Pakistan",25],
    ["Pakistan",30],
    ["Pakistan",18],
    ["Pakistan",22],
    ["Pakistan",27],
    ["Pakistan",35]
    ]

print("\nAfter adding 2 Columns:")
print(df)

# Adding Multiple Rows
multi_rows=pd.DataFrame([{"Name":"TOP","Age":24 ,"Role":"Assaulter","Country":"Mongoliya", "Kills":40 },{"Name":"DOK","Age":26 ,"Role":"IGL","Kills":45,"Country":"Mongoliya" }],index=["Player6","Player7"])
df=pd.concat([df,multi_rows])
print("\nAfter adding 2 Rows:")
print(df)