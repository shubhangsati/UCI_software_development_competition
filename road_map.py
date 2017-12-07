class grid :
	height = 0
	width = 0
	map_graph = []

	def __init__(self, rows, columns):
		self.height = rows
		self.width = columns
		self.map_graph = [["-" for i in range(columns)] for j in range(rows)]

	def add_road(self, start_row, start_column, end_row, end_column):
		if (start_row < 0 or start_row >= self.height or start_column < 0 or end_column >= self.width):
			raise ValueError("[-] Out of bounds input")

		if (start_row == end_row and start_column == end_column):
			raise ValueError("[-] Can't create 0 length road")

		if (start_row != end_row and start_column != end_column):
			raise ValueError("[-] Can't create diagonal roads")

		direction = ""
		polarity = 0
		if (start_row == end_row):
			if (start_column > end_column):
				direction = "l"
				polarity = -1
			else:
				direction = "r"
				polarity = 1

			for index in range(start_column, end_column + 1, polarity):
				if (self.map_graph[start_row][index] != '-'):
					self.map_graph[start_row][index] = 'I'

				else:
					self.map_graph[start_row][index] = direction


		else:
			if (start_row > end_row):
				direction = "u"
				polarity = -1
			else:
				direction = "d"
				polarity = 1

			for index in range(start_row, end_row + 1, polarity):
				if (self.map_graph[index][start_column] != '-'):
					self.map_graph[index][start_column] = 'I'

				else:
					self.map_graph[index][start_column] = direction



	def display(self):
		for x in range(self.width):
			print '-',
		print
		
		for i in self.map_graph:
			for j in i:
				if j == '-':
					print ' ',
				else:
					print j,
			print

		for x in range(self.width):
			print '-',
		print



def test():
	x = grid(10, 10)
	print "New map created\n"
	x.display()
	print "\n"

	x.add_road(3, 4, 3, 9)
	x.add_road(0, 0, 0, 9)
	x.add_road(3, 4, 9, 4)

	print "Three roads added\n"
	x.display()
	print "\n"


if __name__ == "__main__":
	test()