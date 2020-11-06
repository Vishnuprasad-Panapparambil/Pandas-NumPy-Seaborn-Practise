import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mtb
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix

data_income=pd.read_csv('C:/Users/user/PycharmProjects/pythonProject/data_projects/income_casestudy/income(1).csv')
data=data_income.copy()
print(data.info())
print(data.isnull().sum())
summary_num=data.describe()
print(summary_num)
summary_cat=data.describe(include="O")
print(summary_cat)
print(data['JobType'].value_counts())
print(np.unique(data['JobType']))
data=pd.read_csv('C:/Users/user/PycharmProjects/pythonProject/data_projects/income_casestudy/income(1).csv',na_values=[" ?"])
print(data.isnull().sum())

missing=data[data.isnull().any(axis=1)]
print(missing)
data2=data.dropna(axis=0)
print(data2.shape)
corelation=data2.corr()
print(corelation)
print(data2.columns)
gender=pd.crosstab(index=data2["gender"],
                   columns="count",
                   normalize=True)
print(gender)
gender1=pd.crosstab(index=data2["gender"],
                   columns=data2["SalStat"],
                   normalize="index")
print(gender1)
sal_status=sns.countplot(x="SalStat",data=data2)

# reindexing salary status name to 0,1
data2['SalStat']=data2['SalStat'].map({' greater than 50,000':1,' less than or equal to 50,000':0})
print(data2['SalStat'])

# converting character categories to indegers
new_data=pd.get_dummies(data2,drop_first=True)
print(new_data)

# storing the column name
columns_list=list(new_data.columns)
print(columns_list,"\n")

# separates columns from column_list
features=list(set(columns_list)-set(['SalStat']))
print(len(features))
print(len(columns_list))


#storing the output values in y
y=new_data['SalStat'].values
print(y)

x=new_data[features].values
print(x)

# splitting data into train and text
train_x,test_x,train_y,test_y=train_test_split(x,y,test_size=0.3,random_state=0)

# make an instance of the model
logistic=LogisticRegression()


#fitting the values for x and y
logistic.fit(train_x,train_y)
(logistic.coef_)


#prediction from test data
prediction=logistic.predict(test_x)
print(prediction)


confusion_matrix=confusion_matrix(test_y,prediction)
print(confusion_matrix)

accuracy_score=accuracy_score(test_y,prediction)
print(accuracy_score)


from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt


