import turtle
import random
import os

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("sojjy's Space invaders")

#Draw border
border_pen = turtle.Turtle() 
border_pen.hideturtle()
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
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 20

#Make a function to move the player 
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

#Making the player bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("circle")
bullet.speed(0)
bullet.penup()
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.pendown()
#Create keyboard movement
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")


#Create the enemies
enemy_1 = turtle.Turtle()
enemy_1.color("red")
enemy_1.shape("triangle")
enemy_1.penup()
enemy_1.setposition(0, 280)
enemy_1.setheading(270)

enemyspeed = 2


while True:
    
    x = enemy_1.xcor()
    x += enemyspeed
    enemy_1.setx(x)

    if enemy_1.xcor() > 280:
        enemyspeed *= -1

    if enemy_1.xcor() < -280:
        enemyspeed *= -1
    

delay = input("Click Enter To Exit: ")