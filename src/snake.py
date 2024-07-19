from turtle import Turtle
from random import randint

STARTER_LENGTH = 3
RIGHT, UP, LEFT, DOWN = 0, 90, 180, 270
COLOR = "white"
SHAPE = "square"


class Snake:
    def __init__(self) -> None:
        self.segments = []
        self.starter()
        self.head = self.segments[0]
        self.head.shape("arrow")

    def starter(self):
        x_loc, y_loc = 0, 0
        for seg in range(STARTER_LENGTH):
            self.grow(x_loc, y_loc)
            x_loc -= 20

    def grow(self, x_loc, y_loc, heading=0):
        random_color = (
            randint(0, 255) / 255,
            randint(0, 255) / 255,
            randint(0, 255) / 255,
        )

        add_seg = Turtle(shape=SHAPE)
        add_seg.color(random_color)
        add_seg.penup()
        add_seg.goto(x_loc, y_loc)
        add_seg.setheading(heading)
        self.segments.append(add_seg)

    def reset(self):
        for seg in self.segments:
            seg.hideturle()
        self.segments.clear()
        self.starter()
        self.head.shape("arrow")

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            prev_seg = self.segments[seg_num - 1]
            x_loc = prev_seg.xcor()
            y_loc = prev_seg.ycor()
            heading = prev_seg.heading()

            curr_seg = self.segments[seg_num]
            curr_seg.goto(x_loc, y_loc)
            curr_seg.setheading(heading)

        self.head.forward(20)

    def is_tall_eaten(self):
        x_loc = self.head.xcor()
        y_loc = self.head.ycor()

        if x_loc > 300:
            self.head.goto(-300 + 10, y_loc)

        if x_loc < -300:
            self.head.goto(300 - 10, y_loc)

        if y_loc > 300:
            self.head.goto(x_loc, -300 + 10)

        if y_loc < -300:
            self.head.goto(x_loc, 300 - 10)

    def right(self):
        if self.head.heading != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading != UP:
            self.head.setheading(DOWN)
