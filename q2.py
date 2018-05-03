#Read the data
import pandas as pd
df=pd.read_csv('Crimes_-_2001_to_present.csv')

#2.Create a series of the frequency of each type of crime.
total_crimes=df['Primary Type'].value_counts()
# What are the three most common types of crime?

top_3=total_crimes.head(3)
print('Q2. The 3 most common types of crime are: ')
print(top_3)

#What are the three least common?
least_3=total_crimes.tail(3)
print('Q2. The 3 least common types of crime are: ')
print(least_3)
