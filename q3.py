#Read the data
import pandas as pd

df=pd.read_csv('Crimes_-_2001_to_present.csv')

#3. Create a series of the proportion of each type of crime that results in arrest.
#Which crime type is most likely to result in arrest? Hint:

    #First subset the data to rows where Arrest is True.
df_arr=df[df.Arrest == True]
    #Use this to calculate the number of crimes of each type that lead to arrest.
total_arr_crim=df_arr['Primary Type'].value_counts()

    #Divide this by the series you created in 2
total_crimes=df['Primary Type'].value_counts()
ratio_arrest_crime=total_arr_crim/total_crimes

    #Finally, sort the values
print('Q3. The type of crimes that are most likely to result in arrest are: ')
print(ratio_arrest_crime.sort_values().tail(4))
