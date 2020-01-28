import pandas as pd

df =pd.DataFrame()

df=pd.read_excel('Example_Data.xlsx')
print(df.head(10))
print(df.groupby(['Device'])['Data'].head(10))
print(df.loc[df['Time']==0,'Data'])
df['sub'] = df['Data'] - df.loc[df.groupby('Device')['Time'].transform('idxmin'), 'Data'].values

print(df.head(20))
