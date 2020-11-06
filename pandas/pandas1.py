import pandas as pd
result=pd.read_csv("C:/Users/user/PycharmProjects/pythonProject/csvfiles/marks.csv")
result1=result.copy(deep=True)
print(result1)
#number of rows
print(result.index)
#number of columns
print(result.columns)
#size of dataframe
print(result.size)
#dimension of the dataframe
print(result.shape)
#indexing and selecting data
print(result.at[4,'total '])
#indexing and selecting data
print(result.iat[3,3])