import turtle
class Treasure(turtle.Turtle):
    turtle.register_shape("../img/bone.gif")
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("../img/bone.gif")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)
        
    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()
