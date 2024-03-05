#Name: Itai Lavie
#Email: itai.lavie47@myhunter.cuny.edu
#Date: March 5, 2024
#This program completes assignment 13

import turtle

wn = turtle.Screen()
tess = turtle.Turtle()
tess.color("cornflowerblue")
tess.shape("turtle")
tess.pensize(3) 
angle = 72

for _ in range(5):
    tess.forward(100)  # Move forward 100 units
    tess.stamp()       # Stamp the turtle shape at the corner
    tess.left(angle)   # Turn left 72 degrees to form the next side of the pentagon

wn.exitonclick()