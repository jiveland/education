import pandas as pd
import os
wd=os.getcwd()

df=pd.read_excel('Example_Data.xlsx')
print(df.head(10))

df['sub'] = df['Data'] - df.loc[df.groupby('Device')['Time'].transform('idxmin'), 'Data'].values

print(df.head(20))
df.to_csv('out.csv')
