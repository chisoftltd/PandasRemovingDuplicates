# Pandas - Removing Duplicates
# Discovering Duplicates
import pandas as pd 
df = pd.read_csv('data.csv')
print(df.duplicated())

# Removing Duplicates
df.drop_duplicates(inplace = True)
print(df.to_string())
