
# INSERT NEW COLUNM IN PANDAS

import pandas as pd


data = {
    'Student':['Rahul','Mihir','Seela'],
    'Rank': [1,2,3],
    'Marks':[99,88,98]
}

df = pd.DataFrame(data)
print(df)
print()

# INSERT()
# INSERT NEW COLUNM USING INSERT(INDEX, COLUNM_NAME, DATA) METHOD
df.insert(1,'phone',[1111,2222,333332])
print(df)
print()



# ASSIGN()
# ASSIGN IS USED TO INSERT NEW COLUNM AT LAST 
# THIS WILL RETURN NEW ARRAY
df = df.assign(Age = [22,24,21])
print(df)