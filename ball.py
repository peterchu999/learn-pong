from turtle import Turtle

MOVE_DISTANCE = 10

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("circle")
        self.x_move = MOVE_DISTANCE
        self.y_move = MOVE_DISTANCE
        self.move_speed = 0.1

    def move_foward(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.goto(x=0,y=0)
        self.move_speed = 0.1