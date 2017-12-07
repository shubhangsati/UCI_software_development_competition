import pygame, sys
from pygame.locals import *
from road_map import grid


rows = input("Enter number of rows in the map : ")
columns = input("Enter number of columns in the map : ")
rmp = grid(rows, columns)

def main():
	print 'Road description'
	print 'The map is a grid of', rows, ' rows and', columns, 'columns'
	print 'To define a road enter the cell details in the following format :-'
	print '<start_row>, <start_column>, <end_row>, <end_column>'
	print 'rows range from 1 to', rows
	print 'columns range from 1 to', columns
	print 'To end your input enter 0 0 0 0'
	a, b, c, d = map(int, raw_input().split())
	while True:
		if a == 0 and b == 0 and c == 0 and d == 0:
			break
		rmp.add_road(a - 1, b - 1, c - 1, d - 1)
		a, b, c, d = map(int, raw_input().split())

	pygame.init()
	screen = pygame.display.set_mode((columns * 50, rows * 50))
	screen.fill((0, 0, 0,))

	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

		for x in range(columns):
			for y in range(rows):
				if rmp.map_graph[y][x] != '-':
					pygame.draw.rect(screen, (80, 80, 80), (x * 50, y * 50, 50, 50))

		pygame.display.update()


if __name__ == "__main__":
	main()