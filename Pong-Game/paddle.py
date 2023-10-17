from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(1, 5)
        self.shapesize(1, 5)
        self.penup()
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.goto(x_cor, y_cor)
        self.setheading(90)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
