
#  CATEGORY METHODS IN PANDAS

import pandas as pd

data = [10,20,30]
s = pd.Series(data, dtype='category')
print(f'Before : \n{s}')



# ADD NEW CATEGORY

s = s.cat.add_categories(40)
# s[3] = 40              # -->  this will add in when assign but when we try to add 50 then dtype change to object its not add
print(f'\nAfter add 40 : \n{s}')





# REMOVE CATEGORY

s = s.cat.remove_categories(10)
s[3] = 40
# s[4] = 10       # -->  This will change the dtype to object because 10 is no longer a valid category
print(f'\nAfter remove 10 : \n{s}')