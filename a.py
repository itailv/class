#Name: Itai Lavie
#Email: itai.lavie47@myhunter.cuny.edu
#Date: March 24, 2024
#This program completes assignment 35

import pandas as pd

def main():
    # Ask the user for the input file name and the attribute to search by
    file_name = input("Enter file name: ")
    attribute = input("Enter attribute: ")
    
    # Read the data from the input CSV file
    data = pd.read_csv(file_name)
    
    # Validate if the attribute exists in the dataframe
    if attribute not in data.columns:
        print(f"Attribute '{attribute}' not found in the data.")
        return
    
    # Count the occurrences of each unique value in the specified attribute column
    # and sort them to find the 10 worst offenders
    offender_counts = data[attribute].value_counts().head(10)
    
    # Print the results
    print("The 10 worst offenders are:\n")
    print(offender_counts)

if __name__ == "__main__":
    main()