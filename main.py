import turtle

wn = turtle.Screen()
wn.title("Pong :)")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

Paddle_A = turtle.Turtle()
Paddle_A.speed(0)
Paddle_A.shape("square")
Paddle_A.shapesize(stretch_wid=5, stretch_len=1)
Paddle_A.color("white")
Paddle_A.penup()
Paddle_A.goto(-350,0)

Paddle_B = turtle.Turtle()
Paddle_B.speed(0)
Paddle_B.shape("square")
Paddle_B.shapesize(stretch_wid=5, stretch_len=1)
Paddle_B.color("white")
Paddle_B.penup()
Paddle_B.goto(350,0)

Ball = turtle.Turtle()
Ball.speed(0)
Ball.shape("square")
Ball.color("white")
Ball.penup()
Ball.goto(0,0)

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A:0   Player B: 0", align="center",
              font=("Courier", 24, "normal"))
Score_A = 0
Score_B = 0


def pa_up():
    y = Paddle_A.ycor()
    y += 30
    Paddle_A.sety(y)
def pa_down():
    y = Paddle_A.ycor()
    y -= 30
    Paddle_A.sety(y)
def pb_up():
    y = Paddle_B.ycor()
    y += 30
    Paddle_B.sety(y)
def pb_down():
    y = Paddle_B.ycor()
    y -= 30
    Paddle_B.sety(y)
wn.listen()
wn.onkey(pa_up, "w")
wn.onkey(pa_down, "s")
wn.onkey(pb_up, "Up")
wn.onkey(pb_down, "Down")
Ball.dx = 0.2
Ball.dy = 0.2


while True:
    wn.update()

    Ball.setx(Ball.xcor() + Ball.dx)
    Ball.sety(Ball.ycor() + Ball.dy)
    if Paddle_A.ycor() > 250:
        Paddle_A.sety(250)
    if Paddle_A.ycor() < -250:
        Paddle_A.sety(-250)
    if Paddle_B.ycor() > 250:
        Paddle_B.sety(250)
    if Paddle_B.ycor() < -250:
        Paddle_B.sety(-250)
    if Ball.ycor() > 290:
        Ball.sety(290)
        Ball.dy *= -1
    if Ball.ycor() < -290:
        Ball.sety(-290)
        Ball.dy *= -1
    if Ball.xcor() > 390:
        Ball.goto(0, 0)
        Ball.dx *= -1
        Score_B += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(Score_A, Score_B), align="center",
                  font=("Courier", 24, "normal"))

    if Ball.xcor() < -390:
        Ball.goto(0, 0)
        Ball.dx *= -1
        Score_A += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(Score_A, Score_B), align="center",
                  font=("Courier", 24, "normal"))
    if Ball.xcor() > 340 and Ball.ycor() < Paddle_B.ycor() + 50 and Ball.ycor() > Paddle_B.ycor() - 50:
        Ball.dx *= -1
    if Ball.xcor() < -340 and Ball.ycor() < Paddle_A.ycor() + 50 and Ball.ycor() > Paddle_A.ycor() - 50:
        Ball.dx *= -1
