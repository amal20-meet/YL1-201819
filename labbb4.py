class Rectangle(object):
	def __init__(self, width, height):
		self.width = width
		self.height = height
	def Area(self):
		return self.width * self.height
	def perimeter(self):
		return(self.width + self.height) * 2
	def print_prop(self):
		print ("width is" + str(self.width) + ("height is" + str(self.height))
Rectangle1 = Rectangle(10,11)
Rectangle1.print_prop()
	