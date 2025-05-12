from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

window = Screen()
window.bgcolor("black")
window.setup(700,700)
window.title("Snake Game") 
window.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()


game_on = True
while game_on:
    snake.move()
    window.update()
    time.sleep(0.1)
    window.listen()
    window.onkey(snake.up, "Up")
    window.onkey(snake.down, "Down")
    window.onkey(snake.right, "Right")
    window.onkey(snake.left, "Left")
    if snake.head.distance(food) < 15 :
        food.appear()
        snake.extend()
        score.increase_score()
    
    if snake.head.xcor() > 325 or snake.head.xcor() < -325 or snake.head.ycor() > 325 or snake.head.ycor() < -325 :
        game_on = False
        score.game_over()
    
    for segment in snake.turtles[0:-1] :
        if snake.head.distance(segment) < 10 :
            game_on = False
            score.game_over()
       

        

    
window.exitonclick()