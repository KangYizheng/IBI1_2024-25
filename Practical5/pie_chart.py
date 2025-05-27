#plan
#Define UK regional population data
#Define population data for some Chinese provinces
#Sort UK population data
#Sort population data of Chinese provinces
#Print sorted data
#Plot UK regional population pie chart
#Plot population pie chart of Chinese provinces near the Zhejiang province

UK_country_population = [57.11, 3.13, 1.91, 5.45] # England, Scotland, Wales, Northern Ireland
China_country_populations = [41.88,45.28, 61.27,85.15] # Fujian, Jiangxi, Anhui, Jiangsu
sorted_UK = sorted(UK_country_population)  
sorted_China = sorted(China_country_populations)
print(sorted_UK) 
print(sorted_China) 
#plotting the UK regional population pie chart
import matplotlib.pyplot as plt 
labels = "England", "Scotland", "Wales", "Northern Ireland" # Define the labels for each region
sizes = [57.11, 3.13, 1.91, 5.45] # UK regional population data in millions
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue'] #define the colors for each region
explode = (0.1, 0, 0, 0) # explode the first slice (England) for emphasis
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=False, startangle=90)
plt.axis('equal') # Equal aspect ratio ensures that pie chart is a circle.
plt.show() # Display the pie chart
 
# Plotting the population pie chart of Chinese provinces near the Zhejiang province
labels ="Fujian","Jiangxi","Anhui","Jiangsu"# Define the labels for each province
sizes = [41.88,45.28, 61.27,85.15]# Population data for the provinces in millions
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']# Define the colors for each province
explode = (0.1, 0, 0, 0)# Explode the first slice (Fujian) for emphasis
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=False, startangle=90)
plt.axis('equal') # Equal aspect ratio ensures that pie chart is a circle.
plt.show()