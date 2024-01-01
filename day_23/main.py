import time
import random
from turtle import Screen, Turtle
from day_23.player import Player
from day_23.car_manager import CarManager
from day_23.scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect the collision of the turtle with the car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect if the turtle player has reached the top edge
    if player.check_top_edge_reached():
        player.go_to_start()
        car_manager.increase_speed()
        scoreboard.update_level()


screen.exitonclick()

