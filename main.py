import pygame, sys
from pygame.locals import *
from road_map import grid
from traffic_light import trafficlight
from seconds_counter import SecondCounter
from car import car


def main():

	rows = input("Enter number of rows in the map : ")
	columns = input("Enter number of columns in the map : ")
	rmp = grid(rows, columns)

	red = (255, 0, 0)
	green = (0, 255, 0)
	blue = (0, 0, 255)
	yellow = (0, 255, 255)

	intersections = {}
	cars = []

	count = SecondCounter(interval = 1)
	count2 = SecondCounter(interval = 0.5)
	count2.start()
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
	prevfast = count2.peek()

	while True:
		current_time = count.peek()
		currentfast = count2.peek()
		if current_time - previous_time == 1:
			#print current_time
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
				b.tick()
				c.tick()
				d.tick()
				
				pygame.draw.circle(screen, a.color, (a.xposition, a.yposition), 5)
				pygame.draw.circle(screen, b.color, (b.xposition, b.yposition), 5)
				pygame.draw.circle(screen, c.color, (c.xposition, c.yposition), 5)
				pygame.draw.circle(screen, d.color, (d.xposition, d.yposition), 5)

			previous_time = current_time

		print currentfast
		if currentfast - prevfast == 0.5:
			print "fast timer", currentfast
			for ccar in cars:
				pygame.draw.rect(screen, ccar.color, (ccar.xposition, ccar.yposition, 10, 10))
				ccar.tick()
			prevfast = currentfast




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
				if (x >= 50 and x <= columns * 50 and y >= 50 and y <= rows * 50):
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

					elif rmp.map_graph[j][i] != '-':
						count2.pause()
						count.pause()
						posx = i + 1
						posy = j + 1
						c = car((255, 0, 0), '', 0, 0)
						if rmp.map_graph[j][i] in 'lr':
							direction = raw_input("Enter the direction for this car (l or r) : ")
							c.xposition = posx * 50 + 20
							c.direction = direction
							if direction == 'l':
								c.yposition = posy * 50 + 10

							elif direction == 'r':
								c.yposition = posy * 50 + 30

							else:
								print "[i] Default direction left set"
								c.yposition = posy * 50 + 10

						else:
							direction = raw_input("Enter the direction for this car (u or d) : ")
							c.yposition = posy * 50 + 20
							c.direction = direction
							if direction == 'd':
								c.xposition = posx * 50 + 10
								
							elif direction == 'u':
								c.xposition = posx * 50 + 30
								
							else:
								print "[i] Default direction down set"
								c.xposition = posx * 50 + 10

						cars.append(c)

						count2.resume()
						count.resume()



main()