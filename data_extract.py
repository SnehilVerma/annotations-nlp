import os
import pandas as pd
import random

file_name = 'text_classification_dataset.xlsx'
dfs = pd.read_excel(file_name, sheet_name=None)
# print(dfs)
df = dfs['Sheet1']
print(df.type.unique())

values = ['medical','entertainment']
df = df[df.type.isin(values) == False]
rows = df.sample(n=120)
print(rows)

rows = rows.drop('type',1)
writer = pd.ExcelWriter('output_shriya.xlsx')
rows.to_excel(writer)
writer.save()