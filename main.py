import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()

screen.listen()
screen.onkey(player.move_up, 'Up')

gameon = True
while gameon:
    time.sleep(0.1)
    screen.update()

    car.creat_car()
    car.move_car()


screen.exitonclick()
