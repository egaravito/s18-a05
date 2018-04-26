# Assignment 5: Introduction to Pandas

In this assignment you will use the pandas library to explore crime data from the Chicago data portal.

# Instructions

First you'll need to download the dataset. Visit the [data portal page](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2/data). The full dataset is very large so we will just work with the year 2017. To subset it click on Filter and set ["Year is 2017"](filter.png). Download the data as a CSV by clicking "Export" > "CSV" and save it to your assignment directory. It should be about 61mb and 266k rows (use `ls -oh` and `wc -l` at the command line to quickly check).

Write code to answer the following questions in files called `q1.py`,..., `q6.py`. Put the answers to all the questions in a text file called `ANSWERS.txt`. I don't recommend committing the CSV file to your git repository because of the filesize.

# Exercises

1. How many crimes were recorded in 2017? What was the crime rate (defined as the number of crimes per 1000 capita-- find an estimate of Chicago's population online)?

2. Create a series of the frequency of each type of crime. What are the three most common types of crime? What are the three least common?

3. Create a series of the proportion of each type of crime that results in arrest. Which crime type is most likely to result in arrest? Hint:
    - First subset the data to rows where Arrest is True.
    - Use this to calculate the number of crimes of each type that lead to arrest.
    - Divide this by the series you created in 2
    - Finally, sort the values


4. Among those types of crime for which there are at least 1000 incidents, which type is most likely to result in arrest?

    Hint: Create a boolean series whose index is crime type and value is whether the count is at least 1000. Use that to subset your answer to 4 and then sort.

5. What is the number of the community area with the most homicides in 2017? How many were there? What is it's name? (You can find a mapping of community area numbers to names online.)

6. Create a boolean series indicating whether each crime involved a weapon. Then calculate the percentage of crimes involving a weapon. Hint: Look for 'WEAPON' the Description column, but be careful because some descriptions contain 'NO WEAPON'.
