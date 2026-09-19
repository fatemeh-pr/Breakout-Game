from turtle import Turtle

SCORE_FONT = ('Arial', 16, 'normal')
RESULT_FONT = ('Arial', 24, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.turns = 3
        self.penup()
        self.hideturtle()
        self.goto(0, 320)
        self.pendown()
        self.pencolor("white")

        self.update_score(self.score)

    def update_board(self):
        self.clear()
        self.write(f"Score: {self.score} | Turns: {self.turns}", align="center", font=SCORE_FONT)

    def update_score(self, new_score):
        self.score += new_score
        self.update_board()

    def update_turns(self):
        self.turns -= 1
        self.update_board()

    def turns_over(self):
        if self.turns <= 0:
            self.goto(0, 0)
            self.write(f"Game Over", align="center", font=RESULT_FONT)
            return True

    def announce_winner(self):
        self.penup()
        self.goto(0, 0)
        self.pendown()
        self.write(f"You Won!", align="center", font=RESULT_FONT)
