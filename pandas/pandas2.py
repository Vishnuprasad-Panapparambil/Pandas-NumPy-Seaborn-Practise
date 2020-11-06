#two datatypes
#numeric and character
import pandas as pd
import numpy as np
result=pd.read_csv("C:/Users/user/PycharmProjects/pythonProject/csvfiles/marks.csv")
print(result)
#datatypes of columns
print(result.dtypes)
#selecting databased on datatypes
print(result.select_dtypes(exclude=[object]))
#summary of dataframe
print(result.info())
#print unque elements of a column
print(np.unique(result['name']))

