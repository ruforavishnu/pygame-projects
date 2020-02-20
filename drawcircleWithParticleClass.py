

import pygame

(width,height) = (300,200)
background_color = (255,255,255)

class Particle:

		def __init__(self, position, size):
			self.x, self.y = position
			self.size = size
			self.colour = (0,0,255)
			self.thickness = 1

		def display(self):
			pygame.draw.circle(screen, self.colour, (self.x,self.y), self.size, self.thickness)

			


screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Tutorial 1")
screen.fill(background_color)

my_first_particle = Particle((250,80),25)
my_first_particle.display()


pygame.display.flip()

running = True


while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

