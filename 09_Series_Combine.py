
# COMBINE SERIES IN PANDAS

# The combine() method is very useful for element-wise operations with two Series and allows you to define your own logic, like in this case comparing the elements to return the largest value.


import pandas as pd

data1 = [10,5,30,15]
data2 = [6,20,26,40]

s1 = pd.Series(data1)
s2 = pd.Series(data2)

# THIS WILL RETURN LARGEST VALUE 
def demo(x1, x2):
    if x1 > x2:
        return x1
    return x2

# THIS WILL RETURN LARGEST VALUE BY COMBINING BOTH 
res = s1.combine(s2,demo)
print(res)




# CONCATE IN SAME AS REGULAR CONCATE
con = pd.concat((s1,s2),ignore_index=True)
print(con)