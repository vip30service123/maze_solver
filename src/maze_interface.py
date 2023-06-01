from typing import Tuple
from src import constants, maze, maze_solver
from sys import exit

import pygame


def choose_suitable_frame(wide: int = 10, height: int = 10) -> Tuple[int, int]:
    suitable_height = int(constants.HEIGHT / height) * height
    suitable_wide = int(constants.WIDE / wide) * wide
    return (suitable_height, suitable_wide)

def choose_suitable_position(coor):
    return (int(coor[0] / 50) * 50, int(coor[1] / 50) * 50)

def to_matrix_position(coor):
    return (int(coor[0] / 50), int(coor[1] / 50))

def matrix_pos_to_screen_pos(coor):
    return (coor[0] * 50, coor[1] * 50)

class MazeInterface:
    def __init__(self):
        pygame.init()

        self.maze=maze.Maze(height=10, wide=10)

        self.shortest_path = []

        self.white_surface = pygame.Surface((50, 50))
        self.white_surface.fill('White')

        self.black_surface = pygame.Surface((50, 50))
        self.black_surface.fill('Black')

        self.blue_surface = pygame.Surface((50, 50))
        self.blue_surface.fill('Blue')

        self.yellow_surface = pygame.Surface((50, 50))
        self.yellow_surface.fill('Yellow')

        self.green_surface = pygame.Surface((50, 50))
        self.green_surface.fill('Green')

        self.text_font = pygame.font.Font(None, 40)

        self.wall_text = self.text_font.render("Create wall", False, "Red")
        self.start_text = self.text_font.render("Create starting point", False, "Red")
        self.end_text = self.text_font.render("Create ending point", False, "Red")
        self.shortest_path_text = self.text_font.render("Find the shortest path", False, "Red")

        self.mouse_status = ''

    def run(self):
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((800, 500))
        screen.fill("White")

        while True:
            screen.blit(self.wall_text, (500, 0))
            screen.blit(self.start_text, (500, 50))
            screen.blit(self.end_text, (500, 100))
            screen.blit(self.shortest_path_text, (500, 150))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()

                    if pos[0] < 500 and pos[1] < 500:
                        new_pos = choose_suitable_position(pos)
                        matrix_pos = to_matrix_position(pos)
                        if self.mouse_status == 'Create wall':
                            if self.maze.to_list()[matrix_pos[0]][matrix_pos[1]] != "x":
                                self.maze.to_list()[matrix_pos[0]][matrix_pos[1]] = "x"
                                screen.blit(self.black_surface, new_pos)
                            else:
                                self.maze.to_list()[matrix_pos[0]][matrix_pos[1]] = "."
                                screen.blit(self.white_surface, new_pos)
                            self.maze.visualize()
                        elif self.mouse_status == 'Create starting point':
                            if self.maze.to_list()[matrix_pos[0]][matrix_pos[1]] == "o":
                                self.maze.to_list()[matrix_pos[0]][matrix_pos[1]] = "."
                                screen.blit(self.white_surface, new_pos)
                            else:
                                if not self.maze.is_starting_point_available():
                                    self.maze.add_start_point(matrix_pos)
                                    screen.blit(self.yellow_surface, new_pos)
                            self.maze.visualize()
                        elif self.mouse_status == 'Create ending point':
                            if self.maze.to_list()[matrix_pos[0]][matrix_pos[1]] == "0":
                                self.maze.to_list()[matrix_pos[0]][matrix_pos[1]] = "."
                                screen.blit(self.white_surface, new_pos)
                            else:
                                if not self.maze.is_ending_point_available():
                                    self.maze.add_end_point(matrix_pos)
                                    screen.blit(self.green_surface, new_pos)
                            self.maze.visualize()
                        elif self.mouse_status == 'Find the shortest path':
                            shortest_path = maze_solver.MazeSolver(maze=self.maze).get_shortest_path()
                            for vertex in shortest_path:
                                screen.blit(self.blue_surface, matrix_pos_to_screen_pos(vertex))
                        else:
                            continue

                    elif pos[0] > 500 and pos[1] < 50:
                        self.mouse_status = 'Create wall'
                    elif pos[0] > 500 and pos[1] > 50 and pos[1] < 100:
                        self.mouse_status = 'Create starting point'
                    elif pos[0] > 500 and pos[1] > 100 and pos[1] < 150:
                        self.mouse_status = 'Create ending point'
                    elif pos[0] > 500 and pos[1] > 150 and pos[1] < 200:
                        self.shortest_path = maze_solver.MazeSolver(maze=self.maze).get_shortest_path()
                        # for vertex in self.shortest_path:
                        #     screen.blit(self.blue_surface, matrix_pos_to_screen_pos(vertex))
                    else:
                        continue
            
            for vertex in self.shortest_path:
                screen.blit(self.blue_surface, matrix_pos_to_screen_pos(vertex))

            for rowth in range(len(self.maze.to_list())):
                for colth in range(len(self.maze.to_list()[0])):
                    if (rowth, colth) not in self.shortest_path:
                        if self.maze.to_list()[rowth][colth] == "x":
                            screen.blit(self.black_surface, matrix_pos_to_screen_pos((rowth, colth)))
                        elif self.maze.to_list()[rowth][colth] == ".":
                            screen.blit(self.white_surface, matrix_pos_to_screen_pos((rowth, colth)))
                        elif self.maze.to_list()[rowth][colth] == "o":
                            screen.blit(self.yellow_surface, matrix_pos_to_screen_pos((rowth, colth)))
                        elif self.maze.to_list()[rowth][colth] == "0":
                            screen.blit(self.green_surface, matrix_pos_to_screen_pos((rowth, colth)))
                        else:
                            continue
                
            pygame.display.update()
            clock.tick(60)  
