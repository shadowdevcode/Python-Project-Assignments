"""
 Download the dataset from this link ,
("https://raw.githubusercontent.com/Shreyas3108/Weather/master/weather.csv")
Import the data and print the following :
a.) First 5 rows of Dataframe
b.) First 10 rows of the Dataframe
c.) find basic statistics on the particular dataset.
d.) Find the last 5 rows of the dataframe
e.) Extract the 2nd column and find basic statistics on it.
"""

import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/Shreyas3108/Weather/master/weather.csv")

print("---------------Printing first 5 rows of data frame from weather.csv-----------\n")

print(df.head(5))

print("---------------Printing first 10 rows of data frame from weather.csv-----------\n")

print(df.head(10))

print("--------------------Finding basic statistics on dataset-------------------------\n")

print(df.describe())

print("-------------------Finding last 5 rows of the DF------------------------------\n")

print(df.tail(5))

print("----------Extracting the Second Column & Performing Statistics over the data asked -------------- \n")


final_data_extract = df.iloc[:, 2].describe()


print(final_data_extract)
