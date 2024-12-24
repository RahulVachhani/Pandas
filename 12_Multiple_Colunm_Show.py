
# TWO OR MULTIPLE COLUNM SHOW IN PANDAS

# --> df[['c1','c2']]

import pandas as pd

data = {
    'Student':['Rahul','Mihir','Seela'],
    'Rank': [1,2,3],
    'Marks':[99,88,98]
}

df = pd.DataFrame(data)
print(df)
print()

# THIS WILL SHOW PERTICULER GIVEN COLUNM 
print(df[['Marks','Rank']])
print()

# THIS WILL SHOW MULTIPLE COLUNM BY GIVEN SLICING
print(df[df.columns[:2]])





