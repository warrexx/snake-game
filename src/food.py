from turtle import Turtle
from random import randint

FOOD_COLOR = "red"
FOOD_SHAPE = "circle"
FOOD_SIZE = {"len": 0.5, "wid": 0.5}


class Food(Turtle):
    def __init__(self, height: float, width: float) -> None:

        super().__init__()
        self.color(FOOD_COLOR)
        self.shape(FOOD_SHAPE)
        self.shapesize(FOOD_SIZE["len"], FOOD_SIZE["wid"])
        self.penup()

        self.x_range = int(height / 2 - 20)
        self.y_range = int(width / 2 - 20)

        x, y = randint(self.x_range, self.x_range), randint(-self.y_range, self.y_range)
        self.goto(x, y)

    def eaten(self) -> None:
        x, y = randint(self.x_range, self.x_range), randint(-self.y_range, self.y_range)
        self.goto(x, y)
