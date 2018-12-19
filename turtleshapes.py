from turtle import *
import random
import math
class Ball(Turtle):
	def __init__(self,radius,color,speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed(speed)
ball1 = Ball(5,"red",5)
ball2 = Ball(10,"orange",10)
def check_collision(b1,b2):
	x1, y1 = b1.pos()
	x2, y2 = b2.pos()
	r1 = b1.radius
	r2 = b2.radius
	d = math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))
	if r1 + r2>= d:
		print("collision")
	else:
		print("hhhhhh")
	
check_collision(ball1, ball2)
mainloop()

