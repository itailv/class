#Name: Itai Lavie
#Email: itai.lavie47@myhunter.cuny.edu
#Date: March 5, 2024
#This program completes assignment 16

s = input("Enter string: ")
ls = len(s)

for i in range(ls+1):
    print(s[:i])

for i in range(ls):
    print(s[i:])

print("Thank you for using my program!")
