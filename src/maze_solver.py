from maze import Maze
from typing import List


class MazeSolver:
    def __init__(self, maze: Maze = None) -> None:
        if maze:
            self.maze_list = maze.get()
        else:
            self.maze_list = None

    def get_maze(self, maze: Maze) -> None:
        self.maze_list = maze.get()

    def shortest_path(self) -> List[Tuple[int, int]]:
        return [[]]