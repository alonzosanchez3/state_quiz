from turtle import Turtle

class Answer(Turtle):

  def __init__(self,state, x, y):

    super().__init__()
    self.penup()
    self.goto(x, y)
    self.hideturtle()
    self.write(f"{state}")
