import numpy as np 
import pandas as pd 
import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
        
#Reading excel file containing dataset. Displaying for preprocessing

data= pd.read_excel('../input/datasetchitfund/data.xlsx')
data.head()

#Altering column names and deleting first row which contains names
data.rename(columns={'Unnamed: 0':'Month','Unnamed: 1':'Contribution','Unnamed: 2':'Amount won by the bidder','Unnamed: 3':'Chit fund organizer commission','Unnamed: 4':'Net amount recd by Bid winner','Unnamed: 5':'Amount returned to everyone in the group'}, inplace=True)
data.drop(data.index[0],inplace=True)
data.head()

#Calculating the return value for every bidder
bid_return = np.array(data['Net amount recd by Bid winner'])
each_month = np.array(data['Amount returned to everyone in the group'])
for i in each_month:
        bid_return += i
print(bid_return)

#Creating a new column in the dataset with bid return values
data['Bid_return']=bid_return

#Using the lambda function to map out return percentages
sol= data.assign(Return_percentage=lambda x: x.Bid_return * (100/50000))

#Printing results and saving output as .csv file
print("Annualized return of first bidder=",sol.iloc[0,-1])
print("Annualized return of last bidder=",sol.iloc[-1,-1])
sol.to_csv('output.csv')

#Note: solution can also be saved as .xlsx file by using pd.to_excel function
