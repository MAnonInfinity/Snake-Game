from turtle import Screen
import time
from playsound import playsound
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

WIDTH = 600
HEIGHT = 600
FOOD_THRESHOLD = 17

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # When n = 0 then automatic screen updates are off

snake = Snake()
food = Food()
score = ScoreBoard()

screen.update()

screen.listen()
screen.onkey(fun=snake.up, key="w")
screen.onkey(fun=snake.down, key="s")
screen.onkey(fun=snake.left, key="a")
screen.onkey(fun=snake.right, key="d")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Food collision detection
    if snake.head.distance(food) < FOOD_THRESHOLD:
        snake.increase_size()
        food.refresh_food()
        score.increase_score()

    # Wall collision detection
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        game_is_on = False
        score.game_over()
        playsound("sounds/game_over.wav")

    # Tail collision detection
    for i in snake.segments[1:]:
        if snake.head.distance(i) < 10:
            game_is_on = False
            score.game_over()
            playsound("sounds/game_over.wav")

screen.exitonclick()
