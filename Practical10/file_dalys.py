import os
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
os.chdir(r"C:\Users\ASUS\Desktop\第二学期")
# Read the CSV file into a DataFrame.
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
# read just the “Year” column.
Year_column=dalys_data.loc[:,"Year"]
# create a Boolean that is True when the “Year” is “1990”.
a=Year_column==1990
#find exactly the rows i need.
results = dalys_data.loc[a,"DALYs"]
print(results)

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
else:
    print("France has a higher mean DALYs rate than UK.")
# Plotting the DALYs rates for the UK    
plt.plot(uk.Year, uk.DALYs, 'b+')
plt.xticks(uk.Year,rotation=-90)
plt.show()
# The answer to other question 
a= dalys_data.loc[:,"DALYs"]
b=a>=650000
results = dalys_data.loc[b,"Entity"]
print(results)