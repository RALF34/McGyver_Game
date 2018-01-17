"""classes for McGyver game"""

import pygame
import random 
from pygame.locals import * 
from constants import *

class Labyrinth :
	def __init__(self, code_file):
		self.code_file = code_file
		self.position_tools = {'ether':(0,0), 'tube':(0,0), 'needle':(0,0)}

	def display_game(self,position_mcgyver,screen):
		"""Method to display the labyrinth"""	
		pygame.init()
		background = pygame.image.load("green_background.jpg").convert()
		mcgyver = pygame.image.load("mcgyver.png").convert()
		guard = pygame.image.load("guard.png").convert()
		needle = pygame.image.load("needle.png").convert()
		tube = pygame.image.load("plastic_tube.png").convert()
		ether = pygame.image.load("ether.png").convert()
		screen.blit(background,(0,0))
		screen.blit(mcgyver,position_mcgyver)
		screen.blit(guard,((nbr_cells_on_board-1)*lenght_cell,(nbr_cells_on_board-1)*lenght_cell))
		if 'ether' in laby.position_tools.key():
			screen.blit(ether,self.position_tools['ether'])
		if 'tube' in laby.position_tools.key():
			screen.blit(tube,self.position_tools['tube'])
		if 'needle' in laby.position_tools.key():
			screen.blit(needle,self.position_tools['needle'])
		pygame.display.flip()
		wall = pygame.image.load("WALL.png").convert()
		with open(self.code_file, "r") as f:
			i = 0
			for line in f:
				for j in range(len(line)-1):
					if line[j] == 'M':
						screen.blit(wall, (j*lenght_cell,i*lenght_cell))
						pygame.display.flip()
				i += 1


			
	
	
	def placing_tools(self):
		"""Méthod for randomly placing tools that McGyver has to collect in order to make the syringue"""
		needle_correctly_placed, tube_correctly_placed, ether_correctly_placed = False, False, False
		with open(self.code_file, "r") as f:
			lines = f.readlines()
			while not ether_correctly_placed:
				x_cell_ether = random.randint(2,nbr_cells_on_board-2)
				y_cell_ether = random.randint(2,nbr_cells_on_board-2)
				if lines[y_cell_ether][x_cell_ether] == "C":
					self.position_tools['ether'] = (x_cell_ether * lenght_cell , y_ether * lenght_cell) 
					ether_correctly_placed = True
			while not tube_correctly_placed:
				x_cell_tube = random.randint(2,nbr_cells_on_board-2)
				y_cell_tube = random.randint(2,nbr_cells_on_board-2)
				if lines[y_cell_tube][x_cell_tube] == "C"  and  (x_cell_tube , y_cell_tube) != (x_cell_ether , y_cell_ether):
					self.position_tools['tube'] = (x_cell_tube * lenght_cell , y_cell_tube * lenght_cell)
					tube_correctly_placed = True
			while not needle_correctly_placed:
				x_cell_needle = random.randint(2,nbr_cells_on_board-2)
				y_cell_needle = random.randint(2,nbr_cells_on_board-2)
				if lines[y_cell_needle][x_cell_needle] == "C":
					if (x_cell_needle , y_cell_needle) != (x_cell_tube , y_cell_tube):
						if (x_cell_needle , y_cell_needle) != (x_cell_ether , y_cell_ether):
							self.position_tools['needle'] = (x_cell_needle * lenght_cell , y_cell_needle * lenght_cell)
							needle_correctly_placed = True


					



class McGyver:

	def __init__(self):
		self.x_cell = 0
		self.y_cell = 0
		self.x_pixel_pos = 0
		self.y_pixel_pos = 0
		self.objects_found = 0

	
	def turning(self, laby, towards):
		mcgyver = pygame.image.load("mcgyver.png").convert()
		with open(laby.code_file, "r") as f:
			lines = f.readlines()
			if towards == 'right':
				if self.x_cell != (nbr_cells_on_board - 1):
					if lines[self.y_cell][self.x_cell+1] != 'M':
						if (self.x_cell+1,self.y_cell) in laby.position_tools.values():
							self.objects_found += 1
							for key in laby.position_tools.keys():
								if laby.position_tools[key] == (self.x_cell + 1 , self.y_cell):
									laby.position_tools.pop(key)
						self.x_cell += 1
						self.x_pixel_pos = self.x_cell * lenght_cell
		
			if towards == 'left':
				if self.x_cell != 0:
					if lines[self.y_cell][self.x_cell-1] != 'M':
						if [self.x_cell-1,self.y_cell] in laby.position_tools:
							self.objects_found += 1
							for key in laby.position_tools.keys():
								if laby.position_tools[key] == (self.x_cell - 1 , self.y_cell):
									laby.position_tools.pop(key)
						self.x_cell = self.x_cell-1
						self.x_pixel_pos = self.x_cell * lenght_cell
				
			if towards == 'up':
				if self.y_cell != 0:
					if lines[self.y_cell-1][self.x_cell] != 'M':
						if [self.x_cell,self.y_cell-1] in laby.position_tools:
							self.objects_found += 1
							for key in laby.position_tools.keys():
								if laby.position_tools[key] == (self.x_cell , self.y_cell - 1):
									laby.position_tools.pop(key)
						self.y_cell = self.y_cell-1
						self.y_pixel_pos = self.y_cell * lenght_cell
		
			if towards == 'down':
				if self.y_cell != (nbr_cells_on_board - 1):
					if lines[self.y_cell+1][self.x_cell] != 'M':
						if [self.x_cell,self.y_cell+1] in laby.position_tools:
							self.objects_found += 1
							for key in laby.position_tools.key():
								if laby.position_tools[key] == (self.x_cell , self.y_cell + 1):
									laby.position_tools.pop(key)
						self.y_cell += 1
						self.y_pixel_pos = self.y_cell * lenght_cell
				
