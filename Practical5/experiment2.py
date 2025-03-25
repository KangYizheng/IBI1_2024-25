UK_country_population = [57.11, 3.13, 1.91, 5.45] # England, Scotland, Wales, Northern Ireland
China_country_populations = [41.88,45.28, 61.27,85.15] # Fujian, Jiangxi, Anhui, Jiangsu
sorted_UK = sorted(UK_country_population) 
sorted_China = sorted(China_country_populations)
print(sorted_UK) 
print(sorted_China) 
#plotting the data
import matplotlib.pyplot as plt 
labels = "England", "Scotland", "Wales", "Northern Ireland" 
sizes = [57.11, 3.13, 1.91, 5.45] 
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue'] 
explode = (0.1, 0, 0, 0) 
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=False, startangle=90)
plt.axis('equal') 
plt.show()
 
import matplotlib.pyplot as plt
labels ="Fujian","Jiangxi","Anhui","Jiangsu"
sizes = [41.88,45.28, 61.27,85.15]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=False, startangle=90)
plt.axis('equal')
plt.show()