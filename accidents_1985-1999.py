import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

#Read in the data from csv
try:
	df = pd.read_csv('data/airline-safety.csv')
except FileNotFoundError: 
	print("File does not exist")

#Sort the values based on the total accidents
df.sort_values(["incidents_85_99", "fatal_accidents_85_99"], ascending = False , inplace = True)

#Set background of the grid.
sns.set(style = "darkgrid")

#Retrieve figure and axes objects
fig, ax = plt.subplots()

#Total accidents
sns.set_color_codes("pastel")
sns.barplot(x = "incidents_85_99", y = "airline", data = df, label= "Total", color = "b")

#Fatal accidents
sns.set_color_codes("dark")
sns.barplot(x = "fatal_accidents_85_99", y = "airline", data = df, label = "Fatal Accidents", color = "r")

#Legend location
ax.legend(ncol = 2, loc = "lower right", frameon = True)
ax.set(xlim = (0, 80), ylabel = "", xlabel = "Total accidents (1985 - 1999)")

#Display plot
plt.show()


