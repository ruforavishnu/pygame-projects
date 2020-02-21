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

		def bounce(self):
			if(self.x > width - self.size):
				outside_travelled_offset = self.x - (width-self.size)
				self.x = (width - self.size) - outside_travelled_offset
				self.angle = - self.angle

			elif self.x < self.size:
				outside_travelled_offset = self.size - self.x 
				self.x = self.size + outside_travelled_offset
				self.angle = - self.angle

			elif self.y > height - self.size:
				outside_travelled_offset =self.y - (height - self.size)
				self.y = (height - self.size) - outside_travelled_offset
				self.angle = math.pi - self.angle

			elif self.y <  self.size:
				outside_travelled_offset = self.size - self.y
				self.y = self.size + outside_travelled_offset
				self.angle = math.pi - self.angle




screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Particles moving inside screen area with random speed and random angle")
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
		particle.bounce()
		particle.display()
	pygame.display.flip()

