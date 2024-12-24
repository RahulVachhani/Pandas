
# JOINS DATAFRAME IN PANDAS

import pandas as pd


data1 = {
    'ID' : ['S01','S02','S03'],
    'STUDENT' : ['Amit', 'Rohan', 'Mina'],
    'ROLL' : [100,101,102]
}

data2 = {
    'RANK' : [1,2,3],
    'MARKS' : [99,97,95]
}


df1 = pd.DataFrame(data1) 
df2 = pd.DataFrame(data2)

print(f'\nDf1 : \n{df1}')
print(f'\nDf2 : \n{df2}')


# JOIN USING "join()"

join = df1.join(df2)
print(f'\nAfter Join : \n{join}')






# JOIN BASED ON KEYS OR INDEX
# Create two DataFrames
df1 = pd.DataFrame({
    'A': ['A0', 'A1', 'A2'],
    'B': ['B0', 'B1', 'B2']
}, index=['K0', 'K1', 'K2'])

df2 = pd.DataFrame({
    'C': ['C0', 'C1', 'C2'],
    'D': ['D0', 'D1', 'D2']
}, index=['K1', 'K0', 'K2'])

# Join on index
result = df1.join(df2)
print(result)
