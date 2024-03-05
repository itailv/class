#Name: Itai Lavie
#Email: itai.lavie47@myhunter.cuny.edu
#Date: March 5, 2024
#This program completes assignment 14

user_message = input("Enter a message: ")
reversed_message = user_message[::-1]

for char in reversed_message:
    print(f"{char} {char}")