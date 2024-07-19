from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

CANVAS_HEIGHT, CANVAS_WIDTH = 600, 600

screen = Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.screensize(canvheight=CANVAS_HEIGHT, canvwidth=CANVAS_WIDTH)
screen.tracer(0)

border = Turtle()
border.color("white")
border.hideturtle()
border.teleport(-300, -300)
for _ in range(4):
    border.forward(CANVAS_HEIGHT)
    border.left(90)

snake = Snake()
food = Food(CANVAS_HEIGHT, CANVAS_WIDTH)
scoreboard = Scoreboard()


def turn_off() -> None:
    game_is_on = False


screen.listen()
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")


def main_game():
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
        snake.teleport()

        # detect collision with food
        if snake.head.distance(food) < 15:
            food.eaten()
            snake.eat()
            scoreboard.increase_score()

        # detect collision with tail
        if snake.is_tail_eaten():
            snake.reset()
            scoreboard.reset()


if __name__ == "__main__":
    main_game()

screen.exitonclick()
