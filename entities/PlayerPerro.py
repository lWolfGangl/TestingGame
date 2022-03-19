import math
import turtle
class Player(turtle.Turtle):
	turtle.register_shape("../img/dog.gif")
	turtle.register_shape("../img/dog_right.gif")
	def __init__(self,walls):
		turtle.Turtle.__init__(self)
		self.shape("../img/dog.gif")
		self.color("blue")
		self.penup()
		self.speed(0)
		self.gold = 0
		self.walls = walls

	def go_up(self):
		move_to_x = self.xcor()
		move_to_y = self.ycor() + 24

		if (move_to_x, move_to_y) not in self.walls:
			self.goto(move_to_x, move_to_y)
			print(self.xcor()," ",self.ycor())
	def go_down(self):
		move_to_x = self.xcor()
		move_to_y = self.ycor()-24

		if (move_to_x, move_to_y) not in self.walls:
			self.goto(move_to_x, move_to_y)
			print(self.xcor()," ",self.ycor())
	def go_left(self):
		move_to_x = self.xcor() - 24
		move_to_y = self.ycor()

		if (move_to_x, move_to_y) not in self.walls:
			self.goto(move_to_x, move_to_y) 
			self.shape("../img/dog.gif")
			print(self.xcor()," ",self.ycor())
			
	def go_right(self):
		move_to_x = self.xcor() + 24
		move_to_y = self.ycor()
		
		if (move_to_x, move_to_y) not in self.walls:
			self.goto(move_to_x, move_to_y)
			self.shape("../img/dog_right.gif")
			print(self.xcor()," ",self.ycor())
			
	def is_collision(self, other):
		a = self.xcor()-other.xcor()
		b = self.ycor()-other.ycor()
		distance = math.sqrt((a**2)+(b**2))
		if distance < 5:
			return True
		else:
			return False

	def dies(self):
		print("Has Muerto!")
		self.goto(-4800,-4800)
		print("Puntaje final ",self.gold)