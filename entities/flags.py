import turtle
class Flag(turtle.Turtle):
    turtle.register_shape("../img/flag.gif")
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("../img/flag.gif")
        self.color("green")
        self.penup()
        self.speed(0)
        self.gold = 400
        self.goto(x, y)
    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()