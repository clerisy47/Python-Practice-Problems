from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.display_score()

    def increase_score(self, player):
        if player == "l":
            self.l_score += 1
        else:
            self.r_score += 1
        self.clear()
        self.display_score()

    def display_score(self):
        self.goto(-100, 250)
        self.write(self.l_score, align="center", font=("Courier", 50, "normal"))
        self.goto(100, 250)
        self.write(self.r_score, align="center", font=("Courier", 50, "normal"))
