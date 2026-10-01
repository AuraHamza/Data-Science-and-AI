import pandas as pd

df=pd.read_json("Product.json")
print(df.to_string())