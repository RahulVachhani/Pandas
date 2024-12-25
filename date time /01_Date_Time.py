
# DATE TIME IN PANDAS

import pandas as pd


# TIMESTAMP.NOW() --> THIS RETURN CURRENT TIME AND DATE

dt = pd.Timestamp.now()
print(f'\nCurrent Date and Time : {dt}')


# DAYOFWEEK 
dt = pd.Timestamp(year=2024, month=12, day=31, hour=11)

dw = dt.dayofweek
print(f'\nDay of week : {dw}')


# DAYOFYEAR
dy = dt.dayofyear
print(f'\nDay of Year : {dy}')


# DAYINMONTH
dm = dt.daysinmonth
print(f'\nDay in month : {dm}')



# ISLEAPYEAR 
ly = dt.is_leap_year
print(f'\nYear is leap year : {ly}')


# ISMONTHEND   --> DAY = 31 OR 30
me = dt.is_month_end
print(f'\nMonth is end : {me}')


# ISMONTHSTART   --> DAY = 1
ms = dt.is_month_start
print(f'\nMonth is start : {ms}')


# ISYEARSTART   
ys = dt.is_year_start
print(f'\nYear is start : {ys}')


# ISYEAREND
ye = dt.is_year_end
print(f'\nYear is end : {ye}')



