class car:

	direction = ''
	xposition = 0
	yposition = 0
	color = (255, 255, 255)
	valuetoadd = 5

	def __init__(self, color, direction, xpos, ypos):
		self.direction = direction
		self.xposition = xpos
		self.yposition = ypos
		self.color = color

	def tick(self):
		if self.direction == 'l':
			self.xposition -= self.valuetoadd

		elif self.direction == 'r':
			self.xposition += self.valuetoadd

		elif self.direction == 'u':
			self.yposition -= self.valuetoadd

		else:
			self.yposition += self.valuetoadd

