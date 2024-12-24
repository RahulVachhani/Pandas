
# READ CSV FILE IN PANDAS

import pandas as pd


# path = '/home/rahul/Documents/Pandas/csv/students_marks.csv'
path = 'csv/students_marks.csv'        # BOTH ARE WORKING

df = pd.read_csv(path)
print(df)

# print(df['Roll Number'])

