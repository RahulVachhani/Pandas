
# DATAFRAME IN PANDAS

import pandas as pd 


data = {
    'Students' : ['Rahul', 'Meet', 'Amit', 'Kush'],
    'Rank' : [1, 2, 3, 4],
    'Marks' : [99, 97, 95, 94]
}


df = pd.DataFrame(data)

print('Student record : \n',df)
print(type(df))
