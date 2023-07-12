from turtle import Turtle, Screen
import random as r

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="WELCOME TO THE TURTLE RACE GAME", prompt="which turtle will win the race?"
                                                                            " Enter a color: ")
colors = ["red", "green", "blue", "yellow", "orange", "purple"]
y_positions = [-150, -90, -35, 20, 90, 150]
all_turtle = []

for turtle_lineup in range(0, 6):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_lineup])
    new_turtle.goto(x=-230, y=y_positions[turtle_lineup])
    all_turtle.append(new_turtle)


if user_bet:
    is_race_on = True
while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you have won, the {winning_color} turtle is the winner")
            else:
                print(f"you have lost, the {winning_color} turtle is the winner")
        rand_distance = r.randint(0, 10)
        turtle.forward(rand_distance)




screen.exitonclick()

