
#Read the data
import pandas as pd
df=pd.read_csv('Crimes_-_2001_to_present.csv')


#1. How many crimes were recorded in 2017?
crimes= df['ID'].count()
print('Q1. There are ',crimes,' crimes in 2017.')

#What was the crime rate (defined as the number of crimes per 1000 capita-- find an estimate of Chicago's population online)?
#C¡hicago population in 2017 is the 2.736 millions
population=2736000
crime_rate= (crimes*1000)/population
print('Q1. The crime rate is: ', crime_rate)
