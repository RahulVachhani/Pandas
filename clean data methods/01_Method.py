
# BUILT IN METHOD FOR CLEAN THE DATA IN PANDAS

# 1) isnull()
# 2) notnull()
# 3) df.dropna()
# 4) df.fillna(X)

import pandas as pd





path = 'clean data methods/two_column_with_null.csv'

df = pd.read_csv(path)
print(f'\nOriginal Data : \n{df}')



# # isnull()

# # THIS WILL RETURN TRUE AND FALSE IN PLACE OF VALUES , IF VALUE IS NULL OR EMPTY THEN ITS RETURN TRUE AT THAT PLACE
# res = df.isnull()
# print(f'\nNULL Values : \n{res}')



# # THIS IS FOR LARGE DATA TO PRESENT IN STIRNG FORMATE
# print(res.to_string())



# notnull()
# THIS WILL RETURN TRUE IF VALUE IS NOT NULL OR FALSE IF VALUE IN NULL 
res = df.notnull()
print(f'\nNot Null Data : \n{res}')




# df.dropna()
# THIS WILL DELETE ALL ROW WHICH HAVE NULL VALUE AND RETURN REMAINING ROWS

res = df.dropna()
print(f'\nAfter Delete Null Data : \n{res}')




# df.fillna()
# THIS WILL REPLACE NULL VALUE WITH GIVEN VALUE OR PARAMETER
res = df.fillna("ABC")
print(f'\nAfter Replace the Null value with another Value : \n{res}')


#THIS WILL RETURN NOT NULL VALUE COUNT IN EACH COLUNM
print(df.count())



# THIS WILL RETURN COUNT OF NULL VALUE IN EACH COLUNM
null_counts = df.isnull().sum()
print(null_counts)