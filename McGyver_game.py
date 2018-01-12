"""
Game "Trapped in the labyrinthe" 
McGyver has to collect three objects and reach the exit of the labyrinthe 

Python script
Fichiers : ,McGyver_game.py, classes_and_methods.py, constants.py
"""

import pygame
from pygame.locals import *

from classes_and_methods import *
from constants import *

pygame.init()

screen = pygame.display.set_mode((nbr_cells_on_board * lenght_cell, nbr_cells_on_board * lenght_cell))

running = 1
while running:
	
	laby = Labyrinth("struct_laby.txt")

	macGyver = McGyver()

	laby.placing_tools(screen)

	laby.display_game((0,0),screen)

	pygame.time.Clock().tick(30)
	
	for event in pygame.event.get():
		
			
		if event.type == QUIT:
			running = 0
		
		elif event.type == KEYDOWN:
				
			if event.key == K_RIGHT:
				macGyver.turning(laby,'right')
			elif event.key == K_LEFT:
				macGyver.turning(laby,'left')
			elif event.key == K_UP:
				macGyver.turning(laby,'up')
			elif event.key == K_DOWN:
				macGyver.turning(laby,'down')			
			
		
	laby.display_game((mcgyver.pixel_pos,mcgyver.y_pixel_pos),screen)
	

	if (macGyver.x_cell, macGyver.y_cell) == (nbr_cells_on_board-1, nbr_cells_on_board-1) and macGyver.objects_found == 3:
		running = 0



