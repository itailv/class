#Name: Itai Lavie
#Email: itai.lavie47@myhunter.cuny.edu
#Date: March 24, 2024
#This program completes assignment 33

def main():
    # Prompt the user to enter a list of names
    names_string = input("Please enter your list of names: ")
    
    # Split the input string into individual names
    names_list = names_string.split('; ')
    
    print("\nYou entered:\n")
    
    # Process and print each name in the desired format
    for name in names_list:
        last_name, first_name = name.split(', ')
        print(f"{first_name} {last_name}")
    
    print("\nThank you for using my name organizer!")

if __name__ == "__main__":
    main()
