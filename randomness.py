import random
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

number_of_particles = 10
my_particles = []


for n in range(number_of_particles):
		size = random.randint(10,20)
		x = random.randint(size, width-size)
		y = random.randint(size, height-size)

		my_random_particle = Particle((x,y), size)
		my_random_particle.display()
		my_particles.append(Particle((x,y),size))

		





pygame.display.flip()

running = True


while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

