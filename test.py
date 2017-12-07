import pygame, sys
from pygame.locals import *


def main():
	pygame.init()

	DISPLAY=pygame.display.set_mode((500,400),0,32)

	WHITE=(255,255,255)
	blue=(0,0,255)

	DISPLAY.fill(WHITE)

	for x in range(50):
		for y in range(40):
			pygame.draw.rect(DISPLAY, blue, (x * (10 + 1), y * (10 + 1	), 10, 10))


while True:
	main()

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	pygame.display.update()