"""classes for McGyver game"""

import pygame
import random 
from pygame.locals import * 
from constants import *

class Labyrinth :
	def __init__(self, code_file):
		self.code_file = code_file
		self.position_tools = [[0,0],[0,0],[0,0]]

	def display_game(self,position_mcgyver,screen):
		"""Method to display the labyrinth"""	
		pygame.init()
		background = pygame.image.load("green_background.jpg").convert()
		mcgyver = pygame.image.load("mcgyver.png").convert_alpha()
		guard = pygame.image.load("guard.png").convert_alpha()
		needle = pygame.image.load("needle.png").convert_alpha()
		tube = pygame.image.load("plastic_tube.png").convert_alpha()
		ether = pygame.image.load("ether.png").convert_alpha()
		screen.blit(background,(0,0))
		screen.blit(mcgyver,position_mcgyver)
		screen.blit(guard,((nbr_cells_on_board-1)*lenght_cell,(nbr_cells_on_board-1)*lenght_cell))
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

		#screen.blit(ether,(self.position_tools[0][0],self.position_tools[0][1]))
		#screen.blit(tube,(self.position_tools[1][0],self.position_tools[1][1]))
		#screen.blit(needle,(self.position_tools[2][0],self.position_tools[2][1]))
		#pygame.display_flip()

			
	
	
	def placing_tools(self, screen):
		"""Méthod for randomly placing tools that McGyver has to collect in order to make the syringue"""
		needle_correctly_placed, tube_correctly_placed, ether_correctly_placed = False, False, False
		needle = pygame.image.load("needle.png").convert_alpha()
		tube = pygame.image.load("plastic_tube.png").convert_alpha()
		ether = pygame.image.load("ether.png").convert_alpha()
		with open(self.code_file, "r") as f:
			lines = f.readlines()
			while not ether_correctly_placed:
				x_ether = random.randint(2,nbr_cells_on_board-2)
				y_ether = random.randint(2,nbr_cells_on_board-2)
				if lines[y_ether][x_ether] == "C":
					self.position_tools[0][0] = x_ether
					self.position_tools[0][1] = y_ether
					ether_correctly_placed = True
					screen.blit(ether, (x_ether*lenght_cell,y_ether*lenght_cell))
					pygame.display.flip()
			while not tube_correctly_placed:
				x_tube = random.randint(2,nbr_cells_on_board-2)
				y_tube = random.randint(2,nbr_cells_on_board-2)
				if lines[y_tube][x_tube] == "C"  and  (x_tube,y_tube) != (x_ether,y_ether):
					self.position_tools[1][0] = x_tube
					self.position_tools[1][1] = y_tube
					tube_correctly_placed = True
					screen.blit(tube, (x_tube*lenght_cell,y_tube*lenght_cell))
					pygame.display.flip()
			while not needle_correctly_placed:
				x_needle = random.randint(2,nbr_cells_on_board-2)
				y_needle = random.randint(2,nbr_cells_on_board-2)
				if lines[y_needle][x_needle] == "C"  and  (x_needle,y_needle) != (x_tube,y_tube)  and  (x_needle,y_needle) != (x_ether,y_ether):
					self.position_tools[2][0] = x_needle
					self.position_tools[2][1] = y_needle
					needle_corretly_placed = True
					screen.blit(needle,(x_needle * lenght_cell, y_needle * lenght_cell))
					pygame.display.flip()


					



class McGyver:

	def __init__(self):
		self.x_cell = 0
		self.y_cell = 0
		self.x_pixel_pos = 0
		self.y_pixel_pos = 0
		self.objects_found = 0

	
	def turning(self, laby, towards):
		mcgyver = pygame.image.load("mcgyver.png").convert()
		lines = laby.code_file.readlines()
		if towards == 'right':
			if self.x_cell != (nbr_cells_on_board - 1):
				if lines[self.y_cell][self.x_cell+1] != 'M':
					if (self.x_cell+1,self.y_cell) in laby.position_tools:
						self.objects_found += 1
						position_tools.remove("(x_cell+1,y_cell)") 
					self.x_cell += 1
					self.x_pixel_pos = self.x_cell * length_cell
		
		if towards == 'left':
			if self.case_x != 0:
				if lines[self.y_cell][self.x_cell-1] != 'M':
					if (self.x_cell-1,self.y_cell) in laby.position_tools:
						self.objects_found += 1
						position_tools.remove("(x_cell-1,y_cell)")
					self.x_cell -= 1
					self.x_pixel_pos = self.x_cell * lenght_cell
				
		if towards == 'up':
			if self.y_cell != 0:
				if lines[self.y_cell-1][self.x_cell] != 'M':
					if (self.x_cell,self.y_cell-1) in laby.position_tools:
						self.objects_found += 1
						position_tools.remove("(y_cell-1,x_cell)")
					self.y_cell -= 1
					self.y = self.y_cell * lenght_cell
		
		if towards == 'down':
			if self.y_cell != (nbr_cells_on_board - 1):
				if lines[self.y_cell+1][self.x_cell] != 'M':
					if (self.x_cell,self.self.y_cell+1) in laby.position_tools:
						self.objects_found += 1
						position_tools.remove("(y_cell+1,x_cell)")
					self.y_cell += 1
					self.y_pixel_pos = self.y_cell * lenght_cell
				
