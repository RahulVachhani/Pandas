
# METHODS OF PANDAS 

import pandas as pd


# DTYPE
data = {
    'Students' : ['Rahul', 'Meet', 'Amit', 'Kush'],
    'Rank' : [1, 2, 3, 4],
    'Marks' : [99, 97, 95, 94]
}

df = pd.DataFrame(data, index=['s1','s2','s3','s4'])
print(df)
print('\ntype : ',df.dtypes)



# NDIM
print(f'\nDimension :  {df.ndim}')


# SIZE
print(f'\nSize : {df.size}')


# SHAPE
print(f'\nShape : {df.shape}')


# INDEX
print(f'\nIndex : {df.index}')


# T --> Transpose
print(f'\nT --> Transpose : \n{df.T}')


# HEAD   --> BY DEFAULT 5 FIRST DATA RETURN
print(f'\nHead : \n{df.head(2)}')


# TAIL
print(f'\nTail : \n{df.tail(2)}')