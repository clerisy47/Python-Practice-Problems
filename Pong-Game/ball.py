from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.speed("slowest")
        self.x_move = 10
        self.y_move = 10
        self.speed = 0.1

    def reset(self):
        self.goto(0, 0)
        self.bounce_x()

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_move *= -1
        self.speed = 0.1

    def bounce_y(self):
        self.y_move *= -1
        self.speed /= 1.2

