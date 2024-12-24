
# ITERATE ROW IN PANDAS

import pandas as pd

data = {
    'Student':['Rahul','Mihir','Seela'],
    'Rank': [1,2,3],
    'Marks':[99,88,98]
}

df = pd.DataFrame(data)
print(df)
print()


# ITERATING ROWS BY ITERROWS()
for i in df.iterrows():
    print(f'\n{i}')

print()

# ITERATING ROWS BY ITERTUPLES()
for i in df.itertuples():
    print(f'{i}')