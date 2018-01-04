"""classes for McGyver game"""

import pygame, random 
from pygame.locals import * 
from constantes import *

class Labyrinth :
	def __init__(self, code_file):
		self.code_file = code_file
		self.position_tools = ((0,0),(0,0),(0,0))

	def display_laby(self):
		"""Method to display the labyrinth"""	
		pygame.init()
		screen = pygame.display.set_mode((15*30, 15*30))
		background = pygame.image.load("floor.jpg").convert()
		screen.blit(background, (0,0))
		pygame.display.flip()
		wall = pygame.image.load("wall.png").convert()
		with open(self.code_file, "r") as f:
			i = 0
			for line in f:
				for j in range(len(line)-1):
					if line[j] == 'M':
						screen.blit(wall, (j*30,i*30))
						pygame.display.flip()
				i += 1
	    running = True		
		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False

			
	
	
	def display_tools(self, screen):
		"""Méthod for randomly placing tools that McGyver has to collect in order to make the syringue"""
		needle = pygame.image.load("needle.png").convert()
		tube = pygame.image.load("plastic_tube.png").convert()
		ether = pygame.image.load("ether.png").convert()
		needle_correctly_placed, tube_correctly_placed, ether_correctly_placed = False, False, False
		with open(self.code_file, "r") as f:
			lines = f.readlines()
			while not needle_correctly_placed:
				while not tube_correctly_placed:
					while not ether_correctly_placed:
						x_ether, y_ether = random.randint(2,14), random.randint(2,14)
						if lines[y_ether][x_ether] == "C":
							self.position_tools[0] = (x_ether,y_ether)
							ether_correctly_placed = True
							screen.blit(ether, (x_ether*30,y_ether*30))
							pygame.display.flip()
					x_tube, y_tube = random.randint(2,14), random.randint(2,14)
					if lines[y_tube][x_tube] == "C"  and  (x_tube,y_tube) != (x_ether,y_ether):
						self.position_tools[1] = (x_tube,y_tube)
						tube_correctly_placed = True
						screen.blit(tube, (x_tube*30,y_tube*30))
						pygame.display.flip()
                x_needle, y_needle = random.randint(2,14), random.randint(2,14)
				if lines[y_needle][x_needle] == "C"  and  (x_needle,y_needle) != (x_tube,y_tube)  and  (x_needle,y_needle) != (x_ether,y_ether):
					self.position_tools[2] = (x_needle,y_needle)
					needle_corretly_placed = True
					screen.blit(needle,(x_needle * 30, y_needle * 30)) 
					pygame.display.flip()
					

				
            




class McGyver:

	def __init__(self):
		self.x_cell = 0
		self.y_cell = 0
		self.x_pixel_pos = 0
		self.y_pixel_pos = 0
		self.

	
	def moving(self, towards):
		mcgyver = pygame.image.load("mcgyver.png").convert()
		with open("struct_laby.txt","r") as f:
			lines = f.readlines()
			if towards == 'right':
				if self.x_cell != (nbr_cells_on_board - 1):
					if lines[self.y_cell][self.x_cell+1] != 'M':
						if (self.x_cell+1,self.y_cell) in self.position_tools:

						self.x_cell += 1
						self.x_pixel_pos = self.x_cell * length_cell
		
			if towards == 'left':
				if self.case_x != 0:
					if lines[self.y_cell][self.x_cell-1] != 'M':
						if (self.x_cell-1,self.y_cell) in self.position_tools:

						self.x_cell -= 1
						self.x_pixel_pos = self.x_cell * lenght_cell
				
			if towards == 'up':
				if self.y_cell != 0:
					if lines[self.y_cell-1][self.x_cell] != 'M':
						if (self.x_cell,self.y_cell-1) in self.position_tools:

						self.y_cell -= 1
						self.y = self.y_cell * lenght_cell
		
			if towards == 'down':
				if self.y_cell != (nbr_cells_on_board - 1):
					if lines[self.y_cell+1][self.x_cell] != 'M':
						if (self.x_cell,self.self.y_cell+1) in self.position_tools:

						self.y_cell += 1
						self.y_pixel_pos = self.y_cell * lenght_cell
				