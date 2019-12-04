import turtle

wn = turtle.Screen()
wn.title('Pong')
wn.bgcolor('black')
wn.setup(width=1000, height=600)
wn.tracer(0)  # Stops window from updating, manually update it, so we can speed up the game

# Paddle a
paddle_a = turtle.Turtle()
paddle_a.speed(0)  # Speed of animation, not speed of paddle
paddle_a.shape('square')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color('white')
paddle_a.penup()  # does not show lines of movement
paddle_a.goto(-450, 0)

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

# Binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")

# Paddle b
paddle_b = turtle.Turtle()
paddle_b.speed(0) # Speed of animation, not speed of paddle
paddle_b.shape('square')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color('white')
paddle_b.penup() # Turtle draw lines when moving, but we dont need that so use penup
paddle_b.goto(450, 0)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Bindings
wn.listen()
wn.onkeypress(paddle_b_up, 'Up')
wn.onkeypress(paddle_b_down, 'Down')

# Ball
Ball = turtle.Turtle()
Ball.speed(0) # Speed of animation, not speed of paddle
Ball.shape('square')
Ball.color('skyblue')
Ball.penup()
Ball.goto(0, 0)
Ball.dx = 1.4
Ball.dy = -1.4
# Main game loop

# Scoreboard
score = turtle.Turtle()
score.speed(0)
score.penup()
score.hideturtle()
score.color('skyblue')
score.goto(0,270)
score.write("Player 1: 0     Player 2: 0 ", align='center', font=('courier', 20, 'bold'))
score_a = 0
score_b = 0
while True:
    wn.update()

    # Ball movement
    Ball.setx(Ball.xcor() + Ball.dx)
    Ball.sety(Ball.ycor() + Ball.dy)

    # Ball rebound of top and bottom
    if Ball.ycor() > 300:
        Ball.dy *= -1

    if Ball.ycor() < -300:
        Ball.dy *= -1

    # Ball rebound of left and right
    if Ball.xcor() > 500:
        Ball.goto(0,0)
        Ball.dx *= -1
        score_a += 1
        score.clear()
        score.write("Player 1: {}     Player 2: {} ".format(score_a, score_b), align='center', font=('courier', 20, 'bold'))

    if Ball.xcor() < -500:
        Ball.goto(0,0)
        Ball.dx *= -1
        score_b += 1
        score.clear()
        score.write("Player 1: {}     Player 2: {}".format(score_a, score_b), align='center',font=('courier', 20, 'bold'))

    if Ball.xcor() > 450 and (Ball.xcor() < 500) and (paddle_b.ycor() + 50) > Ball.ycor() > (paddle_b.ycor() - 50):
        Ball.dx *= -1

    if Ball.xcor() < -450 and (Ball.xcor() > -500) and (paddle_a.ycor() + 50) > Ball.ycor() > (paddle_a.ycor() - 50):
        Ball.dx *= -1

