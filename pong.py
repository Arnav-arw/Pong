import platform
import turtle
import os
import random

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# AI True or Not
ai_on = True

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 3
ball.dy = 3

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player Blue: 0  Player Red: 0",align="center", font=("Courier", 24, "normal"))

# Actions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 40
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 40
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 40
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 40
    paddle_b.sety(y)


# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main Game
while True:
    wn.update()

    # Moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 380:
        if str(platform.system()) == "Darwin":
            os.system("afplay bounce.wav&")
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player Blue: {}  Player Red: {}".format(
            score_a, score_b), align="center", font=("Courier", 24, "normal"))

    elif ball.xcor() < -390:
        if str(platform.system()) == "Darwin":
            os.system("afplay bounce.wav&")
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player Blue: {}  Player Red: {}".format(
            score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if ball.xcor() < -320 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1

    elif ball.xcor() > 320 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1

    # AI
    if ai_on == True:
        if paddle_a.ycor() < ball.ycor() and abs(paddle_a.ycor() - ball.ycor()) > 20:
            movement = random.randint(0, 25)
            if movement == 0:
                paddle_a_up()
        elif paddle_a.ycor() > ball.ycor() and abs(paddle_a.ycor() - ball.ycor()) > 20:
            movement = random.randint(0, 25)
            if movement == 0:
                paddle_a_down()
