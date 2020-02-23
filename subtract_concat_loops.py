import pandas as pd
import numpy as np

#import dataframe
df=pd.read_excel('Example_Data.xlsx')
print(df.head(200))
dev_list = df['Device'].unique()
#list of devices
print(dev)

dfout=pd.DataFrame()
dfout2 = pd.DataFrame()
# dfout2=pd.DataFrame()
time = 3.2
# interpolation 
for d in dev:
    dfin = df.loc[df['Device']==d]
    
    x=dfin['Time'].values
    y=dfin['Data'].values
    fit = np.polyfit(x,y,2)
    ynew = np.polyval(fit, time)
    addrow = dfin.append({'Time':time,'Device':d,'Data':ynew},ignore_index=True)
    dfout = dfout.append(addrow)
#subtraction of 0 values
for d in dev:
    dfin = dfout.loc[(dfout['Device']==d)]
    dfin['sub'] = dfin['Data']-dfin.loc[dfin['Time']==0,'Data'].values
    dfout2 = dfout2.append(dfin)
    
print(dfout2.head(200))

