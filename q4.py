#Read the data
import pandas as pd
df=pd.read_csv('Crimes_-_2001_to_present.csv')

#4. Among those types of crime for which there are at least 1000 incidents, which type is most likely to result in arrest?
#Hint: Create a boolean series whose index is crime type and value is whether the count is at least 1000. Use that to subset your answer to 3 and then sort.

#Subset the data with at least 1000 incidents
total_crimes=pd.Series(df['Primary Type'].value_counts(), name='Total crimes')
total_arr_crim=pd.Series(df[df.Arrest == True]['Primary Type'].value_counts(), name='Total arrests')
probability=pd.Series((total_arr_crim/total_crimes), name="Probability")


results=(pd.concat([total_crimes, total_arr_crim, probability], axis=1))
print('Q4. The type of crime with more than 1000 incidents that is most likely to result in arrests is: ')
print(results[results['Total crimes']>=1000].sort_values(by='Probability').tail(1))
