"""classes for McGyver game"""

import pygame
import random
from pygame.locals import *
from constants import *

class Labyrinth:

    def __init__(self, code_file):
        """File coding the structure of the labyrinth """
        self.code_file = code_file
        """Dictionnary containing the three objects as keys
        and their positions as values"""
        self.position_tools = {'ether': (0,0), 'tube': (0,0), 'needle': (0,0)}

    def display_game(self, position_mcgyver, screen):
        """Method to display the labyrinth"""
        screen.fill((34,177,76))
        mcgyver = pygame.image.load("mcgyver.png").convert()
        guard = pygame.image.load("guard.png").convert()
        needle = pygame.image.load("needle.png").convert()
        tube = pygame.image.load("plastic_tube.png").convert()
        ether = pygame.image.load("ether.png").convert()
        screen.blit(mcgyver, position_mcgyver)
        screen.blit(guard, ((nbr_cells_on_board-1)*lenght_cell, \
                            (nbr_cells_on_board-1)*lenght_cell))
        """The following tests are telling which tool(s) has been
        found by McGyver, so they don't appears on the screen anymore"""   
        if 'ether' in self.position_tools.keys():
            screen.blit(ether, self.position_tools['ether'])
        if 'tube' in self.position_tools.keys():
            screen.blit(tube, self.position_tools['tube'])
        if 'needle' in self.position_tools.keys():
            screen.blit(needle, self.position_tools['needle'])
        #pygame.display.flip()
        wall = pygame.image.load("WALL.png").convert()
        """Reading of "code_file" and  loop 
        to display the walls of the labyrinth"""
        with open(self.code_file, "r") as f:
            text = f.read()
            i, j, k = 0, 0, 0
            while text[k] != 't':
                if text[k] == '\n':
                    i += 1
                    j = 0
                    k += 1
                elif text[k] == 'M':
                    screen.blit(wall, (j*lenght_cell, i*lenght_cell))
                    #pygame.display.flip()
                    j += 1
                    k += 1
                else:
                    j += 1
                    k += 1
    
    def placing_tools(self):
        """Méthod for randomly placing tools that McGyver has to collect 
        in order to make the syringue """
        needle_correctly_placed = False
        tube_correctly_placed = False 
        ether_correctly_placed = False
        with open(self.code_file, "r") as f:
            lines = f.readlines()
            while not ether_correctly_placed:
                x_cell_ether = random.randint(2, nbr_cells_on_board-2)
                y_cell_ether = random.randint(2, nbr_cells_on_board-2)
                if lines[y_cell_ether][x_cell_ether] == "C":
                    self.position_tools['ether'] = \
                    (x_cell_ether*lenght_cell, y_cell_ether*lenght_cell)
                    ether_correctly_placed = True
            while not tube_correctly_placed:
                x_cell_tube = random.randint(2, nbr_cells_on_board-2)
                y_cell_tube = random.randint(2, nbr_cells_on_board-2)
                if lines[y_cell_tube][x_cell_tube] == "C":
                    """test to prevent the tube and the ether bottle
                    from being at the same place in the labyrinth"""
                    if (x_cell_tube, \
                        y_cell_tube) != (x_cell_ether, y_cell_ether):
                        self.position_tools['tube'] = \
                        (x_cell_tube* lenght_cell, y_cell_tube* lenght_cell)
                        tube_correctly_placed = True
            while not needle_correctly_placed:
                x_cell_needle = random.randint(2, nbr_cells_on_board-2)
                y_cell_needle = random.randint(2, nbr_cells_on_board-2)
                if lines[y_cell_needle][x_cell_needle] == "C":
                    """New tests to avoid having several tools
                    at the same place in the labyrinth""" 
                    if (x_cell_needle, \
                        y_cell_needle) != (x_cell_tube, y_cell_tube):
                        if (x_cell_needle, \
                            y_cell_needle) != (x_cell_ether, \
                                               y_cell_ether):
                            self.position_tools['needle'] = \
                            (x_cell_needle*lenght_cell, \
                             y_cell_needle*lenght_cell)
                            needle_correctly_placed = True
							


class Character:

    def __init__(self):
        self.x_cell = 0
        self.y_cell = 0
        self.x_pixel_pos = 0
        self.y_pixel_pos = 0
        self.tools_found = 0


    def turning(self, laby, towards):
        mcgyver = pygame.image.load("mcgyver.png").convert()
        with open(laby.code_file, "r") as f:
            lines = f.readlines()
            if towards == 'right':
                """Making sure that Mcgyver is not on the 
                right border of the labyrinth"""
                if self.x_cell != nbr_cells_on_board-1:
                    """Making sure that the cell on the
                    right is not a wall ? """
                    if lines[self.y_cell][self.x_cell+1] != 'M':
                        """Making sure whether or not McGyver is
                        moving to a position of a tool"""  
                        if (self.x_pixel_pos+lenght_cell, \
                            self.y_pixel_pos) in \
                        	laby.position_tools.values():
                            self.tools_found += 1
                            """Loop to remove the tool (that McGyver 
                            has just found) from the dictionnary"""
                            for key in laby.position_tools.keys():
                                if laby.position_tools[key] == \
                                (self.x_pixel_pos+lenght_cell, \
                                 self.y_pixel_pos):
                                    laby.position_tools.pop(key)
                                    break
                        self.x_cell += 1
                        self.x_pixel_pos = self.x_cell*lenght_cell
            if towards == 'left':
                """Making sure that McGyver is not on the
                left border of the labyrinth"""
                if self.x_cell != 0:
                    """Making sure that there is no wall""" 
                    if lines[self.y_cell][self.x_cell-1] != 'M':
                        """Checking the presence of a tool on the way"""
                        if (self.x_pixel_pos-lenght_cell, \
                            self.y_pixel_pos) in \
                            laby.position_tools.values():
                            self.tools_found += 1
                            """Loop to remove the tools
                            from the dictionnary"""
                            for key in laby.position_tools.keys():
                            	if laby.position_tools[key] == \
                                (self.x_pixel_pos-lenght_cell, \
                                 self.y_pixel_pos):
                                	laby.position_tools.pop(key)
                                	break
                        self.x_cell = self.x_cell-1
                        self.x_pixel_pos = self.x_cell*lenght_cell
            if towards == 'up':
                """Making sure that McGyver is
                not on the top of the screen"""
                if self.y_cell != 0:
                    """Making sure that there's no wall"""
                    if lines[self.y_cell-1][self.x_cell] != 'M':
                        """Checking the presence of a tool""" 
                        if (self.x_pixel_pos, \
                        	self.y_pixel_pos-lenght_cell) in \
                            laby.position_tools.values():
                            self.tools_found += 1
                            """Removing the element from the dictionnary"""
                            for key in laby.position_tools.keys():
                                if laby.position_tools[key] == \
                                (self.x_pixel_pos, \
                                 self.y_pixel_pos-lenght_cell):
                                	laby.position_tools.pop(key)
                                	break
                        self.y_cell = self.y_cell-1
                        self.y_pixel_pos = self.y_cell*lenght_cell
            if towards == 'down':
                if self.y_cell != nbr_cells_on_board-1:
                    if lines[self.y_cell+1][self.x_cell] != 'M':
                        if (self.x_pixel_pos, \
                            self.y_pixel_pos+lenght_cell) in \
                            laby.position_tools.values():
                            self.tools_found += 1
                            for key in laby.position_tools.keys():
                                if laby.position_tools[key] == \
                                    (self.x_pixel_pos, \
                                     self.y_pixel_pos+lenght_cell):
                                    laby.position_tools.pop(key)
                                    break
                        self.y_cell += 1
                        self.y_pixel_pos = self.y_cell*lenght_cell
				

				