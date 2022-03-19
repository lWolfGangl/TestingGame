import turtle
class Trap(turtle.Turtle):
    turtle.register_shape("../img/hole.gif")
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("../img/hole.gif")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.goto(x, y)
        
    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()
