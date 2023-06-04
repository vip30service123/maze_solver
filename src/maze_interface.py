from sys import exit
from typing import Tuple

import pygame

from src import constants, maze, maze_solver


def _choose_suitable_position(coor) -> Tuple[int, int]:
    return (int(coor[0]/constants.BLOCK_SIZE)*constants.BLOCK_SIZE, 
            int(coor[1]/constants.BLOCK_SIZE)*constants.BLOCK_SIZE)

def _to_matrix_position(coor) -> Tuple[int, int]:
    return (int(coor[0]/constants.BLOCK_SIZE), 
            int(coor[1]/constants.BLOCK_SIZE))

def _matrix_pos_to_screen_pos(coor) -> Tuple[int, int]:
    return (coor[0]*constants.BLOCK_SIZE, coor[1]*constants.BLOCK_SIZE)


class MazeInterface:
    def __init__(self) -> None:
        pygame.init()

        self.maze=maze.Maze(height=constants.MAZE_HEIGHT, 
                            width=constants.MAZE_WIDTH)

        self.shortest_path = []

        self.white_surface = pygame.Surface((constants.BLOCK_SIZE, 
                                             constants.BLOCK_SIZE))
        self.white_surface.fill('White')

        self.black_surface = pygame.Surface((constants.BLOCK_SIZE, 
                                             constants.BLOCK_SIZE))
        self.black_surface.fill('Black')

        self.blue_surface = pygame.Surface((constants.BLOCK_SIZE, 
                                            constants.BLOCK_SIZE))
        self.blue_surface.fill('Blue')

        self.yellow_surface = pygame.Surface((constants.BLOCK_SIZE, 
                                              constants.BLOCK_SIZE))
        self.yellow_surface.fill('Yellow')

        self.green_surface = pygame.Surface((constants.BLOCK_SIZE, 
                                             constants.BLOCK_SIZE))
        self.green_surface.fill('Green')

        self.text_font = pygame.font.Font(None, constants.TEXT_FONT_SIZE)

        self.wall_text = self.text_font.render("Create wall", False, "Red")
        self.start_text = self.text_font.render("Create starting point", 
                                                False, 
                                                "Red")
        self.end_text = self.text_font.render("Create ending point", 
                                              False, 
                                              "Red")
        self.shortest_path_text = self.text_font.render(
            "Find the shortest path", 
            False, 
            "Red")
        self.clear_text = self.text_font.render("Clear", None, "Red")

        self.mouse_status = ''

    def run(self) -> None:
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode(constants.SCREEN_SIZE)
        pygame.display.set_caption('Maze Solver')
        screen.fill("White")

        while True:
            screen.blit(self.wall_text, 
                        (constants.BLOCK_SIZE*constants.MAZE_WIDTH, 0))
            screen.blit(self.start_text, 
                        (constants.BLOCK_SIZE*constants.MAZE_WIDTH, 
                         constants.BLOCK_SIZE))
            screen.blit(self.end_text, 
                        (constants.BLOCK_SIZE*constants.MAZE_WIDTH, 
                         constants.BLOCK_SIZE*2))
            screen.blit(self.shortest_path_text, 
                        (constants.BLOCK_SIZE*constants.MAZE_WIDTH, 
                         constants.BLOCK_SIZE*3))
            screen.blit(self.clear_text, 
                        (constants.BLOCK_SIZE*constants.MAZE_WIDTH, 
                         constants.BLOCK_SIZE*4))

            for rowth in range(len(self.maze.to_list())):
                for colth in range(len(self.maze.to_list()[0])):
                    if (rowth, colth) not in self.shortest_path:
                        if self.maze.to_list()[rowth][colth] == "x":
                            screen.blit(self.black_surface, 
                                        _matrix_pos_to_screen_pos(
                                            (rowth, colth)
                                        ))
                        elif self.maze.to_list()[rowth][colth] == ".":
                            screen.blit(self.white_surface, 
                                        _matrix_pos_to_screen_pos(
                                            (rowth, colth)
                                        ))
                        elif self.maze.to_list()[rowth][colth] == "o":
                            screen.blit(self.yellow_surface, 
                                        _matrix_pos_to_screen_pos(
                                            (rowth, colth)
                                        ))
                        elif self.maze.to_list()[rowth][colth] == "0":
                            screen.blit(self.green_surface, 
                                        _matrix_pos_to_screen_pos(
                                            (rowth, colth)
                                        ))
                        else:
                            continue

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()

                    if (pos[0] < constants.MAZE_HEIGHT*constants.BLOCK_SIZE 
                            and pos[1] < constants.MAZE_WIDTH\
                                *constants.BLOCK_SIZE):
                        new_pos = _choose_suitable_position(pos)
                        matrix_pos = _to_matrix_position(pos)
                        if self.mouse_status == 'Create wall':
                            if self.maze.get_type(matrix_pos) != "x":
                                self.maze.update_type(matrix_pos, "x")
                                screen.blit(self.black_surface, new_pos)
                            else:
                                self.maze.update_type(matrix_pos, ".")
                                screen.blit(self.white_surface, new_pos)
                            self.maze.visualize()
                        elif self.mouse_status == 'Create starting point':
                            if self.maze.get_type(matrix_pos) == "o":
                                self.maze.update_type(matrix_pos, ".")
                                screen.blit(self.white_surface, new_pos)
                            else:
                                if not self.maze.is_starting_point_available():
                                    self.maze.update_type(matrix_pos, "o")
                                    screen.blit(self.yellow_surface, new_pos)
                            self.maze.visualize()
                        elif self.mouse_status == 'Create ending point':
                            if self.maze.get_type(matrix_pos) == "0":
                                self.maze.update_type(matrix_pos, ".")
                                screen.blit(self.white_surface, new_pos)
                            else:
                                if not self.maze.is_ending_point_available():
                                    self.maze.update_type(matrix_pos, "0")
                                    screen.blit(self.green_surface, new_pos)
                            self.maze.visualize()
                        else:
                            continue

                    elif (pos[0] > constants.MAZE_HEIGHT*constants.BLOCK_SIZE 
                            and pos[1] < constants.BLOCK_SIZE):
                        self.mouse_status = 'Create wall'
                    elif (pos[0] > constants.MAZE_HEIGHT*constants.BLOCK_SIZE 
                            and pos[1] > constants.BLOCK_SIZE 
                            and pos[1] < constants.BLOCK_SIZE*2):
                        self.mouse_status = 'Create starting point'
                    elif (pos[0] > constants.MAZE_HEIGHT*constants.BLOCK_SIZE 
                            and pos[1] > constants.BLOCK_SIZE*2 
                            and pos[1] < constants.BLOCK_SIZE*3):
                        self.mouse_status = 'Create ending point'
                    elif (pos[0] > constants.MAZE_HEIGHT*constants.BLOCK_SIZE 
                            and pos[1] > constants.BLOCK_SIZE*3 
                            and pos[1] < constants.BLOCK_SIZE*4):
                        self.shortest_path = maze_solver.\
                                             MazeSolver(maze=self.maze).\
                                             get_shortest_path()
                        for vertex in self.shortest_path:
                            screen.blit(self.blue_surface, 
                                        _matrix_pos_to_screen_pos(vertex))
                    elif (pos[0] > constants.MAZE_HEIGHT*constants.BLOCK_SIZE 
                            and pos[1] > constants.BLOCK_SIZE*4 
                            and pos[1] < constants.BLOCK_SIZE*5):
                        for rowth in range(len(self.maze.to_list())):
                            for colth in range(len(self.maze.to_list()[0])):
                                self.maze.to_list()[rowth][colth] = '.'
                        self.shortest_path = []
                    else:
                        continue

            pygame.display.update()
            clock.tick(60)  
