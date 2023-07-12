import turtle
import winsound

wn = turtle.Screen()
wn.title("uchenna game")
wn.bgcolor('')
wn.setup(width=800, height=600)
wn.tracer(0)

# score
scoreA = 0
scoreB = 0

  # tennis pad A
padA= turtle.Turtle()
padA.speed(0)
padA.shape('square')
padA.color('black')
padA.shapesize(stretch_wid=5, stretch_len=1)
padA.penup()
padA.goto(-350,0)
  # tennis pad B
padB= turtle.Turtle()
padB.speed(0)
padB.shape('square')
padB.color('red')
padB.shapesize(stretch_wid=5, stretch_len=1)
padB.penup()
padB.goto(+350, 0)
  # tennis
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('orange')
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.color("white")
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("courier", 24 , "normal"))

 # lets make it functional😁😂
def padA_up():
    y = padA.ycor()
    y += 50
    padA.sety(y)

def padA_down():
    y = padA.ycor()
    y -= 50
    padA.sety(y)

def padB_up():
    y = padB.ycor()
    y += 50
    padB.sety(y)

def padB_down():
    y = padB.ycor()
    y -= 50
    padB.sety(y)

 #keyboard binding
wn.listen()
wn.onkeypress(padA_up, "w")
wn.onkeypress(padA_down, "s")
wn.onkeypress(padB_up, "Up")
wn.onkeypress(padB_down, "Down")



#let the gaming loop in
while True:
    wn.update()

    # ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #boarder coding
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreA += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(scoreA, scoreB), align="center", font=("courier", 24, "normal"))
        winsound.PlaySound("bounceroll.wav", winsound.SND_ASYNC)

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreB += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(scoreA, scoreB), align="center", font=("courier", 24, "normal"))
        winsound.PlaySound("bounceroll.wav", winsound.SND_ASYNC)

    # bouncing with pad
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < padB.ycor() + 40 and ball.ycor() > padB.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < padA.ycor() + 40 and ball.ycor() > padA.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)



