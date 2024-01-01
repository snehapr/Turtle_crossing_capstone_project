from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.goto(-280, 250)
        self.color("black")
        self.hideturtle()
        self.print_level()

    def print_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER ", align="center", font=FONT)

    def update_level(self):
        self.level += 1
        self.print_level()


