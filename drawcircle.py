

import pygame

(width,height) = (300,200)
background_color = (255,255,255)

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Tutorial 1")
screen.fill(background_color)

pygame.draw.circle(screen, (0,0,255), (50,150), 15, 1)


pygame.display.flip()

running = True


while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

