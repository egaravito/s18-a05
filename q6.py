#Get data
import pandas as pd
df=pd.read_csv('Crimes_-_2001_to_present.csv')
import numpy as np

#6. Create a boolean series indicating whether each crime involved a weapon.
crimes_weapon=df['Description'].str.find('WEAPON')>0
crimes_gun=df['Description'].str.find('GUN')>0
crimes_arm=df['Description'].str.find('ARM')>0

crimes_weapons=(crimes_weapon| crimes_gun | crimes_arm ).sum()
crimes_no_weapon=(df['Description'].str.find('NO WEAPON')>0).sum()
total_crime_weapons=crimes_weapons-crimes_no_weapon

crimes= df['ID'].count()

perc_weapons=format((total_crime_weapons/crimes)*100, '.3f')

print('Q6. The percentage of crimes that use weapons is: ',perc_weapons,'%')
