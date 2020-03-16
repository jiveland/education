import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('export_dataframe_EXAMPLE.csv')

dev_list=['C13','B12']

x_list=['TIME','TIME']
y_list=['DATA_A','DATA_A_SUB']

#iterate through the dev in the dev_list
for dev in dev_list:
    #create dfin for each dev
    dfin = df.loc[(df['DEV_SN']== dev)]
    #find the hours for each
    time = dfin['TIME'].unique()
    time.sort()
    #iterate thorugh the list of plots in the x_list and y_list
    for x,y in zip(x_list,y_list):
        #iterate through the hours

        #select on data for the ith hour
        dfin.sort_values(by=['TIME'], inplace=True)
        
        plt.plot(x, y, data=dfin, label=f'{y}', linestyle='-',marker='o')
        plt.title(f'{dev}')
        plt.xlabel(x)
        plt.ylabel('DATA')
        plt.grid(which='both',axis='both',color='black', linestyle='-', linewidth=0.1)
        plt.gca().legend(loc='best')
        plt.gcf().set_size_inches(6, 6)
       
        
    plt.savefig(f'{dev}_{y}.png',dpi=200)
    plt.show()