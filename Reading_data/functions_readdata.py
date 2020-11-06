import pandas as pd
import numpy as np
data1=pd.read_csv('C:/Users/user/PycharmProjects/pythonProject/csvfiles/marks.csv',na_values=['###'],delimiter=",")
print(data1)
data1.insert(4,"devison"," ")
print(data1)





lt = len(data1['percentage'])

data1['percentage']=data1['percentage'].astype('int64')
print(data1.dtypes)



for i in range(0,lt,1):
    if((data1['percentage'][i])>=75):
        data1['devison'][i]="A"

    elif(50<=(data1['percentage'][i])<75):
        data1['devison'][i]="B"

    elif(25<=(data1['percentage'][i])<50):
        data1['devison'][i]="C"

    elif((data1['percentage'][i])<25):
        data1['devison'][i]="Not Applicable"

    else:
        pass

print(data1)

