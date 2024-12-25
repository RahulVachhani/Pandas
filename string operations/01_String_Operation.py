
# STRING OPERATION IN PANDAS

import pandas as pd


data = ['Rahul','aMiT','MEET']
s = pd.Series(data)
print(f'\n Original Data : \n{s}')


# lower()
print(f'\nLower Case data : \n{s.str.lower()}')

# upper()
print(f'\nUpper Case data : \n{s.str.upper()}')

# title()
print(f'\nTitle Case data : \n{s.str.title()}')


# len()  --> THIS SHOW LENGTH OF ALL VALUE
print(f'\nLen method  : \n{s.str.len()}')


# count()  --> THIS WILL RETERN THE COUNT OF NOT NULL VALUES IN DATASET
print(f'\nNot null Value : {s.count()}')


# cotains()  -->> THIS WILL RETURN TRUE WHERE THIS VALUE MATCH OR EXIST IN ROW
print(f'\nContains : \n{s.str.contains('a')}')


# THIS IS FOR CASE SENSITIVE
print(f'\nContains : \n{s.str.contains('A',case=False)}')