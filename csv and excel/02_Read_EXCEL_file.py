
# READ EXCEL FILE IN PANDAS

# FOR READ EXCEL FILE FIRST INSTALL "openpyxl"  --> pip install openpyxl

import pandas as pd

path = 'csv and excel/students_marks.xlsx'

df = pd.read_excel(path)
print(df)




# WE CAN GIVE INDEX FROM DATA 
import pandas as pd

path = 'csv and excel/students_marks.xlsx'

df = pd.read_excel(path, index_col='Roll Number')
print(df)


# AFTER INDEX THEN WE CAN ACCESS ROW BY THAT INDEX
row = df.loc[1]
print(row)


# THIS WILL SHOW ROW BY INDEX WHICH IS LIKE (0 1 2 3)
print(df.iloc[0])