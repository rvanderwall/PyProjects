from pandas import read_csv

# https://www.fullstackpython.com/blog/learn-pandas-basic-commands-explore-covid-19-data.html

# make sure the file name of the csv matches your file's name!
df = read_csv("covid-19-cases-march-28-2020.csv", encoding="ISO-8859-1")

#print(df.head())
#print(df.tail())
#print(df.count())

# Max value of a field
#print(df.cases.max())

# Various statistics
#print(df.describe())

# Correlation between columns
#print(df.corr())

# 
#print(df.countriesAndTerritories.nunique())

#
df2 = df[df['cases']>=1]
print(df2.count())


print(df2[df2['countriesAndTerritories']=='Vietnam'])

