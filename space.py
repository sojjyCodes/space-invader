import turtle

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


wn = turtle.Screen()
wn.bgcolor("black")
wn.bgpic("space_invaders_background.gif")
wn.title("Space Invaders")

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


#Making the player bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.speed(0)
bullet.penup()
bullet.setpos(0, -230)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.pendown()

#Create keyboard movement
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")


#Create the enemies
enemy = turtle.Turtle()
enemy.color("red")
enemy.penup()
enemy.setposition(0, 280)
enemy.setheading(270)

enemyspeed = 2


while True:
    
    x = enemy.xcor()
    x += enemyspeed
    enemy.setx(x)

    if enemy.xcor() > 280:
        enemyspeed *= -1

    if enemy.xcor() < -280:
        enemyspeed *= -1
    

delay = input("Click Enter To Exit: ")