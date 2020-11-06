import pandas as pd
import numpy as np
import matplotlib.pyplot as mtb

data=pd.read_csv("C:/Users/user/PycharmProjects/pythonProject/csvfiles/passed123.csv")

mtb.scatter(data['name'],data['percentage'],c='green')
mtb.title('student percentage')
mtb.xlabel('name')
mtb.ylabel('percentage')
mtb.show()