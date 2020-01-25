#program imports xlsx files and andd them to df
import pandas as pd
import glob
import os
path = os.getcwd()
file_type ='.xlsx'
files = glob.glob(f'{path}/**/*{file_type}',recursive = True) 
for file in files: 
    print(file)
    
df = pd.DataFrame()
for f in files:
    data = pd.read_excel(f)
    df = df.append(data)
df.head(30)
