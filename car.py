class car:

	direction = ''
	xposition = 0
	yposition = 0
	color = (255, 255, 255)

	def __init__(self, color, direction, xpos, ypos):
		self.direction = direction
		self.xposition = xpos
		self.yposition = ypos
		self.color = color

	def tick(self):
		if self.direction == 'l':
			self.xposition -= 5

		elif self.direction == 'r':
			self.xposition += 5

		elif self.direction == 'u':
			self.yposition -= 5

		else:
			self.yposition += 5