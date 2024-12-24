
#  ITERATING DATAFRAME  TO DIPLAY THE COLUMN

import pandas as pd 


data = {
    'Students' : ['Rahul', 'Meet', 'Amit', 'Kush'],
    'Rank' : [1, 2, 3, 4],
    'Marks' : [99, 97, 95, 94]
}

df = pd.DataFrame(data, index=['s1','s2','s3','s4'])
print(df)



print('\nDisplay colunm name :')
for col in df:
    print(col)
