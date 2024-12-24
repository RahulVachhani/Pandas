
# SERIES METHODS IN PANDAS
import numpy as np
import pandas as pd

data = [10,20,30,40,10]

s = pd.Series(data)

print(f'\nSeries : \n{s}')


# DTYPE
print(f'\nDtype : {s.dtype}')


# NDIM
print(f'\nNdim : {s.ndim}')


# SIZE
print(f'\nSize : {s.size}')


# NAME
data = [10,20,30,40,10, np.nan]
s = pd.Series(data, name = "MySeries" , index=['n1','n2','n3','n4','n5','n6'])
print(s)
print(f'\nName : {s.name}')


# HASNANS   --> THIS WILL RETURN TRUE IF ANY NOT A NUMBER VALUE EXISTS -->(np.nan)
print(f'\nDoes have nan value : {s.hasnans}')



# INDEX
print(f'\nIndex : \n{s.index}')


# HEAD
print(f'\nHead : \n{s.head(3)}')


# TAIL
print(F'\nTail : \n{s.tail(2)}')


# Describe
print(f'\nInfo : \n{s.describe()}')

print(f'\nMemory : \n{s.memory_usage()}')