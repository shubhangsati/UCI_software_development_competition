class trafficlight:

	TIMERED = 0
	TIMEYELLOW = 0
	TIMEGREEN = 0
	totaltime = 0
	color = (255, 0, 0)

	current_timer = 0

	xposition = 0
	yposition = 0
	def __init__(self, TIMERED, TIMEYELLOW, TIMEGREEN, xposition, yposition):
		self.TIMERED = TIMERED
		self.TIMEYELLOW = TIMEYELLOW
		self.TIMEGREEN = TIMEGREEN
		self.xposition = xposition
		self.yposition = yposition
		self.totaltime = self.TIMERED + self.TIMEYELLOW + self.TIMEGREEN

	def tick(self):
		self.current_timer += 1
		if self.current_timer >= 0 and self.current_timer <= self.TIMERED:
			self.color = (255, 0, 0)

		elif self.current_timer > self.TIMERED and self.current_timer <= (self.TIMERED + self.TIMEYELLOW):
			self.color = (255, 126, 0)

		elif self.current_timer > (self.TIMERED + self.TIMEYELLOW):
			self.color = (0, 255, 0)


		self.current_timer %= self.totaltime

	def updatetotaltime(self):
		self.totaltime = self.TIMERED + self.TIMEYELLOW + self.TIMEGREEN