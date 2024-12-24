
# SERIES IN PANDAS

# A Pandas Series is a one-dimensional labeled array capable of holding any data type (integers, strings, floats, Python objects, etc.). It is like a column in a table or a dictionary where each element is associated with a label (index).



import pandas as pd

data1 = [10,20,30,40,50]

s = pd.Series(data1)
print(s)


# # ACCESS ELEMENTS BY INDEX LIKE (0,1,2,3)
print(f'element at index 1 : {s[1]}')
print(f'element at index 3 : {s[3]}')



# ACCESS ELEMENTS BY CUSTOM INDEX
s = pd.Series(data1, index=['A','B','C','D','E'])
print(f'element with custom index A : {s['A']}')
print(f'element with custom index B : {s['D']}')
print(s.loc['A'])


# THIS WILL BY INDEX LIKE 1 2 3 4 LIKE POSITION
print(s.iloc[1])

