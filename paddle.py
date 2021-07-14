from turtle import Turtle

MOVE_DISTANCE = 20

class Paddle(Turtle):
    def __init__(self, initial_coordinate):
        super().__init__()
        self.goto(initial_coordinate)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()

    def move_up(self):
        y_cor = self.ycor()
        x_cor = self.xcor()
        self.goto(x=x_cor, y=y_cor + MOVE_DISTANCE)

    def move_down(self):
        y_cor = self.ycor()
        x_cor = self.xcor()
        self.goto(x=x_cor, y=y_cor - MOVE_DISTANCE)

