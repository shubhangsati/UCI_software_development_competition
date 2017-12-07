import pygame, sys
from pygame.locals import *
from road_map import grid
from traffic_light import trafficlight
from seconds_counter import SecondCounter


def main():

	rows = input("Enter number of rows in the map : ")
	columns = input("Enter number of columns in the map : ")
	rmp = grid(rows, columns)

	red = (255, 0, 0)
	green = (0, 255, 0)
	blue = (0, 0, 255)
	yellow = (0, 255, 255)

	intersections = {}

	count = SecondCounter(interval = 1)
	count.start()

	print 'Road description'
	print 'The map is a grid of', rows, ' rows and', columns, 'columns'
	print 'To define a road enter the cell details in the following format :-'
	print '<start_row>, <start_column>, <end_row>, <end_column>'
	print 'rows range from 1 to', rows
	print 'columns range from 1 to', columns
	print 'To end your input enter 0 0 0 0'
	print 'After you end your input the map will be created with traffic lights at the intersections'
	print 'To edit the traffic lights\' behaviour click on the intersection and enter the details as prompted'
	a, b, c, d = map(int, raw_input().split())
	while True:
		if a == 0 and b == 0 and c == 0 and d == 0:
			break
		rmp.add_road(a - 1, b - 1, c - 1, d - 1)
		a, b, c, d = map(int, raw_input().split())


	for x in range(columns):
		for y in range(rows):
			posx = x + 1
			posy = y + 1
			if rmp.map_graph[y][x] == 'I':
				intersections[(y, x)] = {
					'up' : trafficlight(4, 2, 4, posx * 50 + 25, posy * 50 + 10),
					'right' : trafficlight(4, 2, 4, posx * 50 + 40, posy * 50 + 25),
					'down' : trafficlight(4, 2, 4, posx * 50 + 25, posy * 50 + 40),
					'left' : trafficlight(4, 2, 4, posx * 50 + 10, posy * 50 + 25)
				}

	pygame.init()
	screen = pygame.display.set_mode((columns * 50 + 100, rows * 50 + 100))
	screen.fill((0, 0, 0,))

	previous_time = count.peek()

	while True:
		current_time = count.peek()
		if current_time - previous_time == 1:
			print current_time
			for x in range(columns):
				for y in range(rows):
					if rmp.map_graph[y][x] != '-':
						posx = x + 1
						posy = y + 1
						pygame.draw.rect(screen, (80, 80, 80), (posx * 50, posy * 50, 50, 50))
			for tup in intersections:
				intersection = intersections[tup]
				a, b, c, d = intersection['up'], intersection['right'], intersection['down'], intersection['left']
				a.tick()
				print a.color,
				b.tick()
				c.tick()
				d.tick()
				
				pygame.draw.circle(screen, a.color, (a.xposition, a.yposition), 5)
				pygame.draw.circle(screen, b.color, (b.xposition, b.yposition), 5)
				pygame.draw.circle(screen, c.color, (c.xposition, c.yposition), 5)
				pygame.draw.circle(screen, d.color, (d.xposition, d.yposition), 5)

			previous_time = current_time




		pygame.display.update()


		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

			if pygame.mouse.get_pressed()[0]:
				mpos = pygame.mouse.get_pos()
				x = mpos[0]
				y = mpos[1]
				i = 0
				j = 0
				if (x >= 50 and x <= 1000 and y >= 50 and y <= 500):
					i = x / 50 - 1
					j = y / 50 - 1
					if rmp.map_graph[j][i] == 'I':
						count.pause()
						choice = raw_input("Enter the traffic light you want to edit (left, right, up, down) : ")
						check_choice = (choice != "left" and choice != "right" and choice != "up" and choice != "down")
						while check_choice:
							print "Invalid input"
							x = raw_input("Do you want to try again? Y/N")
							if (x == "Y" or x == "y"):
								choice = raw_input("Enter the traffic light you want to edit (left, right, up, down) : ")
								check_choice = (choice != "left" and choice != "right" and choice != "up" and choice != "down")
							if (x == "N" or x == "n"):
								break

						if not check_choice:
							tred = input("Enter the number of seconds for which this light should be red : ")
							tgreen = input("Enter the number of seconds for which this light should be green : ")
							tyellow = input("Enter the number of seconds for which this light should be yellow : ")
							intersections[(j, i)][choice].TIMERED = tred
							intersections[(j, i)][choice].TIMEGREEN = tgreen
							intersections[(j, i)][choice].TIMEYELLOW = tyellow
							intersections[(j, i)][choice].updatetotaltime()
						count.resume()



main()