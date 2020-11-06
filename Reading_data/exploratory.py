import pandas as pd
import numpy as np

data1=pd.read_csv('C:/Users/user/PycharmProjects/pythonProject/csvfiles/passed123.csv',na_values=['###'],delimiter=",")

data=data1.copy()

#simple cross tabulation
print(pd.crosstab(index=data['class'],columns=data['status'],normalize='columns',dropna=True))
#corelatioon
numerical_data=data1.select_dtypes(exclude=[object])
print(numerical_data.shape)
corr_matrix=numerical_data.corr()
print(corr_matrix)