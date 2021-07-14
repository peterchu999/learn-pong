from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from time import sleep

screen = Screen()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)


right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
scoreboard = Scoreboard()
ball = Ball()

screen.listen()

screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

is_game_on = True

while is_game_on:
    sleep(ball.move_speed)
    ball.move_foward()

    # detect ball bounce at upper and lower wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320 :
        ball.bounce_x()
    elif ball.xcor() > 380:
        ball.reset()
        scoreboard.increase_left_point()
    elif ball.xcor() < -380:
        ball.reset()
        scoreboard.increase_left_point()



    screen.update()

screen.exitonclick()