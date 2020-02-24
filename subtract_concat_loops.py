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

time = [1.5,2.5]
# addrow= {}
data_list =['Data', 'Data Two']
sub_list = ['Data Sub','Data Two Sub']
# interpolation 
for d in dev:
    addrow_list = []

    for data in data_list:
        dfin = df.loc[(df['Device']==d)]
        x=dfin['Time'].values
        y=dfin[data].values
        fit = np.polyfit(x,y,2)
        for t in time:
            yfit = np.polyval(fit, t)
            addrow_list.append({'Time':t,'Device':d,data:yfit})
        
    addrow = dfin.append(addrow_list, ignore_index=True)
    
    dfout = dfout.append(addrow)
print(dfout.head(45))

#subtraction of 0 values

for d in dev:
    dfin = dfout.loc[(dfout['Device']==d)]
    for data,sub in zip(data_list,sub_list):
        dfin[sub] = dfin[data]-dfin.loc[dfin['Time']==0,data].values

    dfout2 = dfout2.append(dfin)
    
print(dfout2.head(20))
