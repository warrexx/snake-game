from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "bold")

SCORE_RECORD = "../data/score.txt"


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.teleport(0, 250)
        self.score = 0
        with open(SCORE_RECORD, mode="r") as file:
            self.high_score = int(file.read())
        self.update_score()

    def increase_score(self) -> None:
        self.score += 1
        self.clear()
        self.update_score()

    def update_score(self) -> None:
        self.write(
            "Score: {self.score} High Score {self.high_score}",
            False,
            align=ALIGNMENT,
            font=FONT,
        )

    def reset(self) -> None:
        if self.score > self.high_score:
            self.high_score: int = self.score
            with open(SCORE_RECORD, mode="w") as file:
                file.write(str(self.high_score))

        self.score = 0
        self.clear()
        self.update_score()
