#plan
#forming a dictionary with programming languages and their popularity percentages
#plot a bar graph to show the popularity of the top 5 programming languages in the dictionary
#check if the language "JavaScript" is present in the dictionary. If it is present, print the percentage of users who use JavaScript.

language_data={"JavaScript":62.3,"HTML":52.9,"Python":51,"SQL":51,"TypeScript":38.5} #dictionary containing the data
# 1. Plot a bar graph to show the popularity of the top 5 programming languages in the dictionary.
print(language_data)
import matplotlib.pyplot as plt
# Extracting the keys and values from the dictionary
languages = list(language_data.keys()) 
percentages = list(language_data.values())

plt.bar(languages, percentages)
plt.xlabel('Programming Languages')
plt.ylabel('Percentage of Users')
plt.title('Popularity of Top 5 Programming Languages')
plt.show()

language="JavaScript" #language to be searched
# 2. Check if the language "JavaScript" is present in the dictionary. If it is present, print the percentage of users who use JavaScript.
if language in language_data:
    print(f"the percentage of {language} is {language_data[language]}")
else:
    print(f"{language} is not present in the dictionary")