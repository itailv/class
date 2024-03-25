#Name: Itai Lavie
#Email: itai.lavie47@myhunter.cuny.edu
#Date: March 24, 2024
#This program completes assignment 30

import pandas as pd
import matplotlib.pyplot as plt

# Ask the user for input and output file names
input_file = input("Enter name of input file: ")
output_file = input("Enter name of output file: ")

# Read the data from the input file
data = pd.read_csv(input_file)

# Calculate the fraction of the total population that are children
data['Fraction Children'] = data['Total Children in Shelter'] / data['Total Individuals in Shelter']

# Plot the fraction of the total population that are children over time
plt.figure(figsize=(10, 6))  # Optional: Adjusts the figure size for better readability
plt.plot(data['Date of Census'], data['Fraction Children'], marker='o', linestyle='-', color='blue')
plt.title('Fraction of Total Population that are Children Over Time')
plt.xlabel('Date of Census')
plt.ylabel('Fraction Children')
plt.xticks(rotation=45)  # Rotates the x-axis labels for better readability
plt.tight_layout()  # Adjusts subplot params so that the subplot(s) fits in to the figure area

# Save the plot to the specified output file
plt.savefig(output_file)