from turtle import *

wn = Screen()
wn.title("PyPong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle a
paddle_a = Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle b
paddle_b = Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = Turtle()
ball.speed(0)
ball.shape('circle')
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = -0.2

def paddle_a_up():
  y = paddle_a.ycor()
  y += 20
  paddle_a.sety(y)

def paddle_a_down():
  y = paddle_a.ycor()
  y -= 20
  paddle_a.sety(y)

def paddle_b_up():
  y = paddle_b.ycor()
  y += 20
  paddle_b.sety(y)

def paddle_b_down():
  y = paddle_b.ycor()
  y -= 20
  paddle_b.sety(y)

wn.listen()
wn.onkeypress(paddle_a_up, 'w')
wn.onkeypress(paddle_a_down, 's')
wn.onkeypress(paddle_b_up, 'Up')
wn.onkeypress(paddle_b_down, 'Down')

while True:
  wn.update()

  ball.setx(ball.xcor() + ball.dx)
  ball.sety(ball.ycor() + ball.dy)

  if ball.ycor() > 290:
    ball.sety(290)
    ball.dy *= -1
  if ball.ycor() < -290:
    ball.sety(-290)
    ball.dy *= -1
  if ball.xcor() > 390:
    ball.goto(0, 0)
    ball.dx *= -1
  if ball.xcor() < -390:
    ball.goto(0, 0)
    ball.dx *= -1
  