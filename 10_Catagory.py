
# CATeGORY IN PANDAS

import pandas as pd

# IN SERIES 

# its used distinct value 
data = [10,20,30]
s = pd.Series(data, dtype='category')
print(s)


# IN DATAFRAME

data1 = {
    'Cat1': list('abcd'),
    'Cat2' : list('efgh')
}

df = pd.DataFrame(data1,dtype='category')
print(df)
print(df.dtypes)




# WITHOUT AND WITH CATEGORY

# Without category dtype (using regular string)
data1 = ['a', 'b', 'a', 'c', 'b', 'a']
s1 = pd.Series(data1)

# With category dtype
s2 = pd.Series(data1, dtype='category')

print(s1.memory_usage(deep=True))  # Memory usage of s1
print(s2.memory_usage(deep=True))  # Memory usage of s2
