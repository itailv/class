#Name: Itai Lavie
#Email: itai.lavie47@myhunter.cuny.edu
#Date: March 24, 2024
#This program completes assignment 26

import pandas as pd

# Function to compute the average and maximum population for a borough
def compute_population_stats(borough_name, data):
    # Extract population data for the specified borough
    borough_data = data[borough_name]
    
    # Calculate average and maximum population
    average_population = borough_data.mean()
    maximum_population = borough_data.max()
    
    return average_population, maximum_population

# Main program
def main():
    # Read the NYC historical population data
    pop = pd.read_csv('/mnt/data/nycHistPop.csv', skiprows=5)
    
    # Prompt the user for the borough name
    borough_name = input("Enter borough: ").strip()

    # Validate the entered borough name
    if borough_name not in pop.columns:
        print(f"Borough name '{borough_name}' is not valid. Please enter one of the following: {list(pop.columns)[1:-1]}")
        return
    
    # Compute the average and maximum population
    average_population, maximum_population = compute_population_stats(borough_name, pop)
    
    # Print out the results
    print("Average population: ", average_population)
    print("Maximum population: ", maximum_population)

# Execute the main program
if __name__ == "__main__":
    main()

