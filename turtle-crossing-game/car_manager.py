# TODO: Turtle va random fayllarini import qilish
# TODO: blocklar yaratish
# TODO: move() va increase_speed() metodini qo'shish

from turtle import Turtle
import random

COLORS = ["red", "blue", "green", "purple", "yellow", "orange"]

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_cars = []
        self.car_speed = 0

    def make_car(self, number_car):
        random_number = random.randint(1, number_car)
        if random_number == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-250, 280))
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(2 + self.car_speed)

            if car.xcor() < -400:
                car.hideturtle()

    def increase_speed(self):
        self.car_speed += 1
