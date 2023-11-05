from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

#inheritance demonstration (scoreboard is subclass of turtle)
class Scoreboard(Turtle):

    #setting up scoreboard
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    #displaying text
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    #display game over
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    #updating score after food collision
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()