import pandas as pd 

data = [100,150,200,250,300]
print("In Python:")
print(data)

series=pd.Series(data)
print("\nUsing Pandas")
print(series)

# series1ize indexing 
series1=pd.Series(data , index=['Hamza','Ali','Sara','Nocki','Falak'])
print("\nseries1ized Index:")
print(series1)
print("\nPrinting using LOC Sara is at:",series1.loc['Sara'])

print("\nPrinting by applying condition >200")
print(series1[series1>200])

print("\nUsing Dictionray:")

Calories ={"Day1":1400 , "Day2":2100 , "Day3":1700}
series2=pd.Series(Calories)
print(series2)
print("\nPrinting by applying condition >200")
print(series2[series2<2000])
