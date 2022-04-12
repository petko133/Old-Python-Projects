from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from targets import Target
from scoreboard import Score

x_position = [-183, -138, -93, -48, -3, 42, 87, 132, 177]

screen = Screen()
screen.title("Breakout Game")
screen.bgcolor("black")
screen.setup(height=600+8, width=400+4)
screen.tracer(0)

paddle = Paddle(0, -280)
target = Target()

for n in range(9):
    target.create_target(x_cor=x_position[n], y_cor=80, color="yellow")
    target.create_target(x_cor=x_position[n], y_cor=100, color="yellow")
    target.create_target(x_cor=x_position[n], y_cor=120, color="green")
    target.create_target(x_cor=x_position[n], y_cor=140, color="green")
    target.create_target(x_cor=x_position[n], y_cor=160, color="orange")
    target.create_target(x_cor=x_position[n], y_cor=180, color="orange")
    target.create_target(x_cor=x_position[n], y_cor=200, color="red")
    target.create_target(x_cor=x_position[n], y_cor=220, color="red")

screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")

ball = Ball()
total_score = Score()

game_on = True

while game_on:
    screen.update()
    ball.move()

    if ball.xcor() > 190 or ball.xcor() < -190:
        ball.bounce()

    if ball.ycor() > 290:
        ball.bounce_paddle()

    if ball.distance(paddle) < 50 and ball.ycor() < -270:
        ball.bounce_paddle()

    for n in target.all_target:
        if ball.distance(n) < 25:
            n.goto(500, 500)
            ball.bounce_paddle()
            a = total_score.scoreboard()

        if ball.ycor() < -300:
            game_on = False
            total_score.game_over()

screen.exitonclick()