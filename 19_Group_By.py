
#  GROUP BY IN PANDAS

import pandas as pd

data = {
    'Student':['Rahul','Mihir','Seela','Mihir','Rahul','hemansu'],
    'Rank': [1, 3, 2, 4, 5,6],
    'Marks':[89, 78, 88, 89, 78,75]
}

df = pd.DataFrame(data)

# GROUPBY(colunm_name)
res = df.groupby('Student')      

# THIS WILL SHOW FIRST DATA 
print(res.first())
print()


# ITERATE GROUP AND SHOW DATA BASED ON SAME STUDENT
for name, group in res:
    print(f'\n{name}')
    print(group)



# GROUP BY STUDENT AND DISPLAY --> ITS SHOW LIKE {'Mihir': [1, 3], 'Rahul': [0, 4], 'Seela': [2], 'hemansu': [5]}  WITH INDEX LIKE [1,2]
print()
print(df.groupby('Student').groups)


# AGGREGATE WITH GROUP BY
print(df.groupby('Student').agg('size'))


# print()
# grouped = df.groupby('Student')['Marks'].sum()
# print(grouped)
# print()

# grouped_multiple = df.groupby('Student')['Marks'].agg(['sum', 'mean', 'max'])
# print(grouped_multiple)
# print() 