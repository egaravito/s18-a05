#Get data
import pandas as pd
df=pd.read_csv('Crimes_-_2001_to_present.csv')

#5. What is the number of the community area with the most homicides in 2017?
areas_homicides=df[df['Primary Type']=='HOMICIDE']['Community Area'].value_counts()
homicides=areas_homicides.reset_index().sort_values(by='Community Area')
homicides.columns=['Comunity Area', 'Homicides']
top1=homicides.tail(1).iloc[0]

#print(top1)
print('Q5. The area with the most homicides in 2017 is',top1['Comunity Area'])
print('Q5. This area has ',top1['Homicides'], 'homicides in 2017')
print('Q5. The name of this community ares is Austin')
#How many were there?
#What is the community area's name? (You can find a mapping of community area numbers to names online.)
#25=Austin
