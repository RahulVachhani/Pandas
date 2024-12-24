
# DELETE COLUNM IN PANDAS

import pandas as pd

data = {
    'Student':['Rahul','Mihir','Seela'],
    'Rank': [1,2,3],
    'Marks':[99,88,98]
}

df = pd.DataFrame(data)
print(df)
print()



# DELETE COLUNM
# # DROP() WILL DELETE COLUNM AND RETURN REMAINING DATA
# df = df.drop('Marks', axis='columns')   # axis = 1 same as axis='columns'
# print(df)



# DELETE ROW
# THIS WILL DELETE ROW DATA
df = df.drop(0, axis='index')   # THIS WILL DELETE DATA OF INDEX 0    
print(df)