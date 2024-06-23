from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []

    def creat_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            car = Turtle()
            car.color(random.choice(COLORS))
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            y = random.randint(-250, 250)
            car.goto(300, y)
            self.all_cars.append(car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)


