import pandas as pd
import numpy as np
result=pd.read_csv("C:/Users/user/PycharmProjects/pythonProject/csvfiles/marks.csv")
print(result)
result1=(result['percentage'].replace("thirty",30))
print(result1)
#to detect missing values
print(result.isnull().sum())

