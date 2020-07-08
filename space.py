import turtle
import random
import os

wn = turtle.Screen()
wn.bgcolor("red")
wn.title("sojjy's Space invaders")
#Draw border
border_pen = turtle.Turtle() 
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()
#Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("turtle")
player.penup()
player.setposition(0, -280)
player.setheading(90)
player.pendown()

playerspeed = 20

def move_left():
    x = player.xcor()
    x-= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

#Create keyboard movement
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")

#Create the enemies
enemy_1 = turtle.Turtle()
enemy_1.color("black")
enemy_1.shape("triangle")
enemy_1.penup()
enemy_1.setposition(-180, 280)
enemy_1.setheading(270)
enemy_1.pendown()

#Creating the second enemy
enemy_2 = turtle.Turtle()
enemy_2.color("black")
enemy_2.shape("triangle")
enemy_2.penup()
enemy_2.setposition(15, 280)
enemy_2.setheading(270)
enemy_2.pendown()

#creating the third enemy
enemy_3 = turtle.Turtle()
enemy_3.color("black")
enemy_3.shape("triangle")
enemy_3.penup()
enemy_3.setposition(180, 280)
enemy_3.setheading(270)
enemy_3.penup()

delay = input("Press enter to finish") 