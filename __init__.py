import numpy as np
import pandas as pd
import topsispy as tp
import sys

df=pd.read_csv(sys.argv[1])
y=df['Fund Name']
df.drop(['Fund Name'],axis=1,inplace=True)
df

df.values
w=sys.argv[2]
w=[int(i) for i in w.split(",")]
impact=sys.argv[3]
impact=[1 if i=='+' else -1 for i in impact]

x=tp.topsis(df.values.tolist(),w,impact)
temp=x[1]
temp

df['Topsis Score']=temp
df

df["Rank"] = df["Topsis Score"].rank(ascending=False)
df

df['Fund Name']=y
first_column = df.pop('Fund Name')
df.insert(0, 'Fund Name', first_column)
df

df.to_csv(sys.argv[4],index=False)

