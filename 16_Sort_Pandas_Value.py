
# SORTING IN PANDAS DATAFRAME

import pandas as pd


data = {
    'Student':['Rahul','Mihir','Seela'],
    'Rank': [1,3,1],
    'Marks':[89,78,88]
}


df = pd.DataFrame(data, index=['s1','s2','s3'])
print(df)


# SORT_VALUES()

# IN ASCENDING ORDER
print(f'\nSorted Data IN ASCENDING : \n{df.sort_values(['Rank'])}')


# IN DESCENDING ORDER
print(f'\nSorted Data IN DESCENDING : \n{df.sort_values(by=['Rank','Marks'],ascending=False)}')


# THIS IS FOR SORT DATA BASED ON RANK AND IF RANK ARE SAME THEN SORT BY MARKS IN DESCENDING ORDER
print(f'\nSorted Data IN ASCENDING with Rank And Marks : \n{df.sort_values(by=['Rank','Marks'], ascending=[True,False])}')




# # REFERENCE CODE
# # Sort by Score (ascending) and Age (descending)
# sorted_df = df.sort_values(by=['Score', 'Age'], ascending=[True, False])
# print(sorted_df)
