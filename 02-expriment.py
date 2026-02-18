#Working with Pandas DataFrame
import pandas as pd

data = {'Name':['A','B','C'], 'Marks':[80,90,75]}
df = pd.DataFrame(data)

print(df)
print("Average Marks:", df['Marks'].mean())
