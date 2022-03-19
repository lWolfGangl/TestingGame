
import math
import turtle
import random


class Enemy(turtle.Turtle):
    turtle.register_shape("../img/catleft.gif")
    turtle.register_shape("../img/catright.gif")
    def __init__(self, walls,ewalls, x, y):
        turtle.Turtle.__init__(self)
        self.shape("../img/catright.gif")
        self.color("red")
        self.penup()
        self.speed(0)
        self.gold = 25
        self.walls = walls
        self.ewalls=ewalls
        self.goto(x, y)
        self.direction = random.choice(["up", "down", "left", "right"])


    def move(self):
        if self.direction == "up":
            dx = 0
            dy = 24
        elif self.direction == "down":
            dx = 0
            dy = -24
        elif self.direction == "left":
            dx = -24
            dy = 0
            self.shape("../img/catleft.gif")
        elif self.direction == "right":
            dx = 24
            dy = 0
            self.shape("../img/catright.gif")
        else: 
            dx = 0
            dy = 0

               
        #Calculate the spot to move to
        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy

        #Check if the space has a walls
        if (move_to_x, move_to_y) not in self.walls and (move_to_x, move_to_y) not in self.ewalls:
            self.goto(move_to_x, move_to_y)
        else:
            self.direction = random.choice(["up", "down", "left", "right"])

        turtle.ontimer(self.move, t=random.randint(100, 300))

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()

    def is_close (self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt ((a ** 2) + (b ** 2))

        if distance < 75:
            return True
        else: 
            return False



            

