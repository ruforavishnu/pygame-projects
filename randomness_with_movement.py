import random
import math
import pygame

(width,height) = (300,200)
background_color = (255,255,255)

class Particle:

		def __init__(self, position, size):
			self.x, self.y = position
			self.size = size
			self.colour = (0,0,255)
			self.thickness = 1
			self.speed = 0.01
			self.angle = 0


		def display(self):
			pygame.draw.circle(screen, self.colour, (int(self.x),int(self.y)), self.size, self.thickness)

		def move(self):
			self.x += math.sin(self.angle) * self.speed
			self.y -= math.cos(self.angle) * self.speed




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
		my_random_particle.speed = random.random()
		my_random_particle.angle = random.uniform(0, math.pi*2)

		my_particles.append(my_random_particle)





running = True


while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill(background_color)
	for particle in my_particles:
		particle.move()
		particle.display()
	pygame.display.flip()

