import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
new_turtle = Turtle()
screen = Screen()
screen.setup(width=500, height=408)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y = -125
all_turtles = []

for index in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x=-200, y=y)
    y += 50
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You Won")
            else:
                print(f"You Lost! The winning turtle is {winning_color}")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()