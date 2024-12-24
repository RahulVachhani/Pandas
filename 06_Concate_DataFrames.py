
# CONCATENATION  

import pandas as pd


# WITHOUT INDEX
data1 = {
    'ID' : ['S01','S02','S03'],
    'STUDENT' : ['Amit', 'Rohan', 'Mina'],
    'ROLL' : [100,101,102]
}

data2 = {
    'ID' : ['S04','S05','S06'],
    'STUDENT' : ['Rita', 'Kirti', 'kiran'],
    'ROLL' : [103,104,105]
}


df1 = pd.DataFrame(data1) 
df2 = pd.DataFrame(data2)

print(f'\nDf1 : \n{df1}')
print(f'\nDf2 : \n{df2}')



# con = pd.concat((df1,df2))
# print(con)

con = pd.concat((df1,df2), ignore_index=True)
print(f'\nCon : \n{con}')





# WITH INDEX  
data1 = {
    'ID' : ['S01','S02','S03'],
    'STUDENT' : ['Amit', 'Rohan', 'Mina'],
    'ROLL' : [100,101,102]
}

data2 = {
    'ID' : ['S04','S05','S06'],
    'STUDENT' : ['Rita', 'Kirti', 'kiran'],
    'ROLL' : [103,104,105]
}


df1 = pd.DataFrame(data1,index=['S1','S2','S3']) 
df2 = pd.DataFrame(data2,index=['S4','S5','S6'])

print(f'\nDf1 : \n{df1}')
print(f'\nDf2 : \n{df2}')



con = pd.concat((df1,df2))
print(con)