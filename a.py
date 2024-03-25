#Name: Itai Lavie
#Email: itai.lavie47@myhunter.cuny.edu
#Date: March 24, 2024
#This program completes assignment 34

def main():
    # Ask the user for the hour of the day in 24-hour format
    hour = int(input("Enter hour (in 24 hour time): "))
    
    # Determine and print the appropriate greeting based on the hour
    if hour < 12:
        print("Good Morning")
    elif hour < 17:  # This implicitly means hour is 12 or greater but strictly less than 17
        print("Good Afternoon")
    else:
        print("Good Evening")

if __name__ == "__main__":
    main()