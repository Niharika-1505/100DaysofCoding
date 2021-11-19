import time
from turtle import Screen
from score import Score
from snake import Snake
from food import Food

screen = Screen()
snake = Snake()
food = Food()
score = Score()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        score.increment_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.xcor() < -280 or snake.head.ycor() > 280:
        score.reset_score()
        snake.reset_snake()

    # Detect collision with tail/body
    for segments in snake.segments[1:]:
        if snake.head.distance(segments) < 10:
            score.reset_score()
            snake.reset_snake()
