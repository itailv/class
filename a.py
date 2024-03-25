#Name: Itai Lavie
#Email: itai.lavie47@myhunter.cuny.edu
#Date: March 24, 2024
#This program completes assignment 26

# Libraries for plotting and data processing:
import matplotlib.pyplot as plt
import pandas as pd

# Open the CSV file and store in pop
pop = pd.read_csv('nycHistPop.csv', skiprows=5)

# Prompt the user for the borough name and output file name
borough_name = input("Enter borough name: ").strip()
output_file_name = input("Enter output file name: ").strip()

# Check if the entered borough name is valid
if borough_name not in pop.columns:
    print(f"Borough name '{borough_name}' is not valid. Please enter one of the following: {list(pop.columns)[1:-1]}")
else:
    # Compute the fraction of the population in the specified borough, and save as new column:
    pop['Fraction'] = pop[borough_name]/pop['Total']

    # Create a plot of year versus fraction of pop. in the specified borough (with labels):
    plt.figure(figsize=(10, 6)) # Optional: Adjust the figure size for better readability
    plt.plot(pop['Year'], pop['Fraction'], marker='o', linestyle='-', color='blue')
    plt.title(f'Fraction of Population in {borough_name} Over Time')
    plt.xlabel('Year')
    plt.ylabel(f'Fraction of Population in {borough_name}')
    plt.grid(True) # Optional: Adds a grid for better readability

    # Save to the specified output file:
    plt.savefig(output_file_name)

    # Important note to self to ensure compliance with assignment requirements:
    # Removed plt.show() to prevent execution errors in the cloud grading environment.
