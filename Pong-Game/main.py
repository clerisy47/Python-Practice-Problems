# Creates a multiplayer Pong Game
import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
screen = Screen()
l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)
ball = Ball()
scoreboard = Scoreboard()
screen.bgcolor("black")
screen.tracer(0)
screen.setup(800, 600)
screen.listen()
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
game_is_on = True
while game_is_on:
    time.sleep(ball.speed)
    screen.update()
    # Collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Collision with the paddle
    if (ball.xcor() > 320 and ball.distance(r_paddle) < 50) \
            or (ball.xcor() < -320 and ball.distance(l_paddle) < 50):
        ball.bounce_x()
    # Touching left or right wall
    elif ball.xcor() > 370:
        ball.reset()
        scoreboard.increase_score("l")
    elif ball.xcor() < -370:
        ball.reset()
        scoreboard.increase_score("r")
    ball.move()
screen.exitonclick()
