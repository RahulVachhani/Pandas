
# REMOVE WHITE SPACE IN PANDAS

import pandas as pd


data = ['Rahul', '\nMahek\n', 'Kiran\t']

s = pd.Series(data)
print(f'\nBefore Data : \n{s}')


# strip()
s1 = s.str.strip()
print(f'\nAfter remove all white space : \n{s1}')



# lstrip()
s2 = s.str.lstrip()
print(f'\nAfter remove all left side white space : \n{s2}')


# rstrip()
s3 = s.str.rstrip()
print(f'\nAfter remove all right side white space : \n{s3}')
