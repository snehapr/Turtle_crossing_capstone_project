from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            random_position_y_axis = random.randint(-250, 250)
            new_car.penup()
            new_car.goto(300, random_position_y_axis)
            random_color = random.choice(COLORS)
            new_car.shape("square")
            new_car.color(random_color)
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.speed)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT


