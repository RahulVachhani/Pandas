
# STATISTICAL FUNCTIONS IN PANDAS

import pandas as pd

data = {
    'Marks': [10,20,30,40,50,70],
    'Student' : ['Rahul', 'Mahek', 'kunal', 'jainil', 'Mihir',None]
}

df = pd.DataFrame(data)
print(f'\nData : \n{df}')



# SUM()   --> THIS WILL ADD ALL VALUE AND RETURN SUM OF THAT COLUNM, IF ITS STRING THEN ITS CONCATE THEN

# sum = df.sum()
# print(sum)

AllMarks = df['Marks'].sum()
print(f'\nMarks Sum : {AllMarks}')


# COUNT()  --> THIS WILL RETURN NOT EMPTY VALUES COUNT
non_empty = df.count()
print(f'\nCount of Non Empty Value : \n{non_empty}')



# MAX() --> THIS IS ONLY WORK FOR INTEGER
max = df['Marks'].max()
print(f'\nMax  of mark is : {max}')


# MIN() --> THIS IS ONLY WORK FOR INTEGER
max = df['Marks'].min()
print(f'\nMin of mark is : {max}')


# MEAN() -->    AVERAGE
mean = df['Marks'].mean()
print(f'\nMean of mark is : {mean}')


# MEADIAN() -->    
median = df['Marks'].median()
print(f'\nMedian of mark is : {median}')


# STD() --> STANDARD DERIVATION 
std = df['Marks'].std()
print(f'\nStandard Derivation of mark is : {std}')


# DESCRIBE()
des = df.describe()
print(f'\nDescription of data : \n{des}')