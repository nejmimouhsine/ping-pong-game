import turtle

wind = turtle.Screen() # initialize screen
wind.title("Ping Pong Game")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0) # stop the window from updating automatically

# player 1
player1 = turtle.Turtle() # initliaze turtle object(shape)
player1.speed(0) # set the speed of the animation
player1.shape("square") # set the shape of the object
player1.color("blue") # set the color of the shape
player1.shapesize(stretch_wid=5, stretch_len=1) # stretch the shape to meet the size
player1.penup() # stops the object from drawing lines 
player1.goto(-350, 0) # set the position of the object

# player 2
player2 = turtle.Turtle()
player2.speed(0)
player2.shape("square")
player2.color("red")
player2.shapesize(stretch_wid=5, stretch_len=1)
player2.penup()
player2.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = 1

# functions
def player1_up():
  y = player1.ycor() # get the y coordinate of the player
  y += 20 # increase y by 20
  player1.sety(y) # set the player the new y coordinate

def player1_down():
  y = player1.ycor()
  y -= 20
  player1.sety(y)

def player2_up():
  y = player2.ycor()
  y += 20
  player2.sety(y)

def player2_down():
  y = player2.ycor()
  y -= 20
  player2.sety(y)

# keyboard bindings
wind.listen() # tell the window to expect keyboard input
wind.onkeypress(player1_up, "w") # call player1_up on click on w
wind.onkeypress(player1_down, "s") # call player1_down on click on s
wind.onkeypress(player2_up, "Up")
wind.onkeypress(player2_down, "Down")

# main game loop
while True:
  wind.update() # updates the screen everytime the loop run

  # move the ball
  ball.setx(ball.xcor() + ball.dx) # ball starts at 0 and everytime loops run--->+1 xaxis  
  ball.sety(ball.ycor() + ball.dy) # ball starts at 0 and everytime loops run--->+1 yaxis

  # border check, top border +300px, bottom border -300px, ball is 20px
  if ball.ycor() > 290: # if ball is at top border
    ball.sety(290) # set ball at 290 y coordinate
    ball.dy *= -1 # reverse direction of the ball, making +1 --> -1

  if ball.ycor() < -290: # if ball is at bottom border
    ball.sety(-290)
    ball.dy *= -1
  
  if ball.xcor() > 390: # if ball is at right border
    ball.goto(0, 0) # return ball to center
    ball.dx *= -1 # reverse the x direction

  if ball.xcor() < -390: # if ball is at left border
    ball.goto(0, 0)
    ball.dx *= -1

  if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < player2.ycor() + 40 and ball.ycor() > player2.ycor() -  40):
    ball.setx(340)
    ball.dx *= -1

  if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < player1.ycor() + 40 and ball.ycor() > player1.ycor() -  40):
    ball.setx(-340)
    ball.dx *= -1