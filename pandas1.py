import pandas as pd
data = pd.read_csv('us_army_death1.csv')
#show the first few rows of the data
print(data.head())
# get the total number of records (each row represents a record)
print(len(data))
# get statistical summary of the numerical column of the data
print(data.describe())
# refer to a single field in the entire data 
print(data['Age'][5])
# manipulate the data
d2 = data['Service']+'Nigeria'
print(d2)


