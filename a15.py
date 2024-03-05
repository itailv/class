#Name: Itai Lavie
#Email: itai.lavie47@myhunter.cuny.edu
#Date: March 5, 2024
#This program completes assignment 15

import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("blue")
tess.shape("turtle")

for _ in range(5):
    num = int(input("Enter a number: "))
    tess.left(num)
    tess.forward(100)

wn.exitonclick()
