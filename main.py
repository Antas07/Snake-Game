from turtle import Screen,Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Score




w = Screen()
w.setup(width=700, height=700)
w.bgcolor('black')
w.title("My Snake Game")
w.tracer(0)


border = Turtle(shape='square')
border.color('brown')
border.penup()
border.goto(-290, -290)
border.pendown()
border.pensize(10)
for i in range(4):
    border.forward(580)
    border.left(90)
border.hideturtle()


snake1 = Snake()
food = Food()
score = Score()

w.listen()
w.onkey(snake1.up, "Up")
w.onkey(snake1.down, "Down")
w.onkey(snake1.left, "Left")
w.onkey(snake1.right, "Right")
game_is_on = True
while game_is_on:
    w.update()
    time.sleep(0.1)
    snake1.move()

    # Detect collision with Food
    if snake1.head.distance(food) < 15:
        score.increase_score()
        food.refresh()
        snake1.extend_snake()

    # Detect collision with wall
    if snake1.head.xcor() > 280 or snake1.head.xcor() < -280 or snake1.head.ycor() > 280 or snake1.head.ycor() < -280:
        score.reset()
        snake1.reset()

    # Detect collision with tail
    for segment in snake1.segments[1:]:
        if snake1.head.distance(segment) < 10:
            score.reset()
            snake1.reset()
if score.game_score > 10:
    w.update()
w.mainloop()
