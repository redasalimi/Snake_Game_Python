from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(0.5,0.5)
        self.appear()

    def appear(self):
        random_x = random.randint(-330, 330)
        random_y = random.randint(-330, 330)
        self.goto(random_x, random_y)
