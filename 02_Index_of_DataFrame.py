
# INDEX OF DATAFRAME

import pandas as pd 


data = {
    'Students' : ['Rahul', 'Meet', 'Amit', 'Kush'],
    'Rank' : [1, 2, 3, 4],
    'Marks' : [99, 97, 95, 94]
}


# THIS WILL GIVE NAME TO ALL INDEX 
df = pd.DataFrame(data, index=['RowA','RowB','RowC','RowD'])

print('Students records : \n', df)
print()


# THIS WILL ACCESS THAT DATA BY THAT INDEX
print(df.loc['RowA'])  # THIS WILL SHOW ALL DATA OF THAT INDEX
print()


print(df.loc['RowA','Students']) # THIS WILL SHOW PERTICULER COLUMN DATA OF THAT INDEX
print()

# THIS WILL SHOW ALL DATA OF STUDENTS COLUNM
print(df['Students'])

