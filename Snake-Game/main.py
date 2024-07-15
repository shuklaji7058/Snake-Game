
from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("🐍Naagin Ka Khel")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

game_is_on = False  # Flag to check if the game has started


def start_game():
    global game_is_on
    game_is_on = True


# Update key press handlers to start the game
screen.listen()
screen.onkey(lambda: (snake.up(), start_game()), "Up")
screen.onkey(lambda: (snake.down(), start_game()), "Down")
screen.onkey(lambda: (snake.left(), start_game()), "Left")
screen.onkey(lambda: (snake.right(), start_game()), "Right")

while True:
    screen.update()
    if game_is_on:
        time.sleep(0.1)
        snake.move()

        # Detect collision with food.
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # Detect collision with wall.
        if snake.head.xcor() > 280:
            snake.head.setx(-280)
        elif snake.head.xcor() < -280:
            snake.head.setx(280)
        elif snake.head.ycor() > 280:
            snake.head.sety(-280)
        elif snake.head.ycor() < -280:
            snake.head.sety(280)

        # Detect collision with tail.
        for segment in snake.segments:
            if segment == snake.head:
                pass
            elif snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()

screen.exitonclick()
