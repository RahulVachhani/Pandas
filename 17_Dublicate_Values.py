

# FIND AND REMOVE DUBLICATE VALUES OR ENTIES IN PANDAS

import pandas as pd


data = {
    'Student':['Rahul','Mihir','Seela','Rahul','Mihir'],
    'Rank': [1, 3, 2, 1, 3],
    'Marks':[89, 78, 88, 89, 78]
}

df = pd.DataFrame(data)
print(f'\nOriginal Data : \n{df}')


# THIS WILL RETURN TRUE IF THAT DATA OR ROW IS DUBLICATE 
res = df.duplicated()
print(f'\nDublicated Data : \n{res}')


# THIS WILL SHOW THAT ROW DATA
dublicated_row = df[res]
print(f'\nDublicated Rows : \n{dublicated_row}')
print(f'\nDublicated Rows : \n{dublicated_row['Student']}')





# REMOVE DUBLICATE DATA
res = df.drop_duplicates()
print(f'\nAfter remove dublicate data : \n{res}')


# THIS IS RETURN COUNT OF SAME VALUE IN THAT COLUNM
name_counts = df['Student'].value_counts()
print(name_counts)