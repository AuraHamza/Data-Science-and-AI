import pandas as pd 

df =pd.read_csv("Cricketers.csv")
print(df.to_string())

# Higher Average
Highest_avg=df[df["Average"]>=50]
print("\nHigher Batting Avg:","\n",Highest_avg.to_string())

# Where Country ==Pakistan
country_wise=df[df["Country"]=="Pakistan"]
print("\nPlayer whoose Country is Pakistan:","\n",country_wise.to_string())

# Filter AND SELECTION
print("\nFilter AND SELECTION:")
print(df[df["Rating"]>9.5][["Country","Role","Rating"]])
