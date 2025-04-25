import os
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
os.chdir(r"C:\Users\ASUS\Desktop\第二学期\IBI1_2024-25\Practical10")
# Read the CSV file into a DataFrame.
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
lines_10= dalys_data.loc[0:9,"Year"]# read the first 10 lines of the DataFrame.
# Display the first 10 lines of the DataFrame.
print(lines_10)
# the 10th year of DALYs data is 82624.94.

# read just the “Year” column.
Year_column=dalys_data.loc[:,"Year"]
# create a Boolean that is True when the “Year” is “1990”.
a=Year_column==1990
#find exactly the rows i need.
results_1 = dalys_data.loc[a,"DALYs"]# get the unique values of the DALYs column.
print(results_1)

uk = dalys_data.loc[dalys_data.Entity=="United Kingdom", ["DALYs", "Year"]]
france = dalys_data.loc[dalys_data.Entity=="France", ["DALYs", "Year"]]
# calculate the mean DALYs rates for the UK and France.
uk_mean = uk["DALYs"].mean()
france_mean = france["DALYs"].mean()
# Display the mean DALYs rates for the UK and France.
print(f"UK mean DALYs rate: {uk_mean}")
print(f"France mean DALYs rate: {france_mean}")
if uk_mean > france_mean:# compare the mean DALYs rate of UK and France.
    print("UK has a higher mean DALYs rate than France.")
elif uk_mean < france_mean:
    print("France has a higher mean DALYs rate than UK.")
else:
    print("UK and France have the same mean DALYs rate.")
# UK has a higher mean DALYs rate than France.
# Plotting the DALYs rates for the UK    
plt.plot(uk.Year, uk.DALYs, 'b+')
plt.xticks(uk.Year,rotation=-90)
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.title("DALYs in the UK")
plt.show()




# The answer to other question 
# read the “DALYs” column.
dalys_column= dalys_data["DALYs"]
# create a Boolean that is True when the “DALYs” is greater than or equal to 650000.
b=dalys_column>=650000
# find the rows that are True.
results_2 = dalys_data.loc[b,["Entity"]]
final_results = results_2["Entity"].unique() # get the unique values of the countries.
# Display the countries with DALYs rates greater than or equal to 650000.
#Only Rwanda has a DALYs rate greater than or equal to 650000.
print(f'Countries with DALYs rates greater than or equal to 650000:{final_results}')