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

def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()


#Set the scoreboard
scoreboard = 0

#Create the window
wn = turtle.Screen()
wn.bgcolor("black")
wn.bgpic("space_invaders_background.gif")
wn.title("Space Invaders")
wn.register_shape('player1.gif')
wn.register_shape('invader.gif')

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
player.shape('player1.gif')
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
bullet.hideturtle()

bulletspeed = 20

bulletstate = "ready"

#Create keyboard movement
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")


#Create the enemies
enemy = turtle.Turtle()
enemy.shape("invader.gif")
enemy.penup()
enemy.setposition(0, 280)
enemy.setheading(270)


#Create the enemy bullet
#bullet2 = turtle.Turtle()
#bullet2.color("red")
#bullet2.shape("triangle")
#bullet2.speed(0)
#bullet2.penup()  #Working on them later
#bullet2.setpos(0, +230)
#bullet2.setheading(270)
#bullet2.shapesize(0.5, 0.5)
#bullet2.hideturtle()
enemyspeed = 2
enemy_bullet_speed = 20

while True:
    
    x = enemy.xcor()
    x += enemyspeed
    enemy.setx(x)

    if enemy.xcor() > 280:
        enemyspeed *= -1

    if enemy.xcor() < -280:
        enemyspeed *= -1

    #Move the bullet and make it shoot
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

delay = input("Click Enter To Exit: ")