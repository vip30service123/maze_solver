from typing import List, Tuple
import random


class MazeContainer:
    '''
    Just to use __contains__ function lol
    '''
    def __init__(self, height: int = 0, wide: int = 0, maze: List[List] = None) -> None:
        if (height != 0 or wide != 0) and maze != None:
            raise Exception("Maze is already created")

        if not maze:
            if height == 0 or wide == 0:
                raise Exception("Height or Wide is missing")
            self.maze = [['.' for _ in range(wide)] for _ in range(height)]
            self.height = height
            self.wide = wide
        else:
            self.maze = maze
            self.height = len(self.maze)
            self.wide = len(self.maze[0])
    
    def __contains__(self, coor: Tuple[int, int]) -> bool:
        if coor[0] < self.height and coor[0] >= 0 and coor[1] < self.wide and coor[1] >= 0:
            return True
        return False

    def get(self):
        return self.maze


class Maze:
    def __init__(self, height: int = 0, wide: int = 0, maze: List[List] = None) -> None:
        self.maze = MazeContainer(height=height, wide=wide, maze=maze)

    def _is_valid_maze(self) -> bool:
        '''
        Check if maze contains starting point and ending point 
        '''
        check = [0, 0]
        for row in self.maze.get():
            if 'o' in row:
                check[0] += 1
            if '0' in row:
                check[1] += 1
        return check == [1, 1]

    def get_starting_point(self) -> Tuple[int, int]:           
        for rowth in range(len(self.maze.get())):
            for colth in range(len(self.maze.get()[rowth])):
                if self.maze.get()[rowth][colth] == 'o':
                    return (rowth, colth)
        raise Exception("Missing starting point")

    def get_ending_point(self) -> Tuple[int, int]:           
        for rowth in range(len(self.maze.get())):
            for colth in range(len(self.maze.get()[rowth])):
                if self.maze.get()[rowth][colth] == '0':
                    return (rowth, colth)
        raise Exception("Missing ending point")

    def add_wall(self, coor: Tuple[int, int]) -> None:
        if coor in self.maze:
            self.maze[coor[0]][coor[1]] = 'x'

    def add_start_point(self, coor: Tuple[int, int]) -> None:
        if coor in self.maze:
            self.maze[coor[0]][coor[1]] = 'o'

    def add_end_point(self, coor: Tuple[int, int]) -> None:
        if coor in self.maze:
            self.maze[coor[0]][coor[1]] = '0'

    def change_specific_position(self, coor: Tuple[int, int], position_type: str) -> None:
        if coor in self.maze:
            self.maze.get()[coor[0]][coor[1]] = position_type

    def to_list(self) -> List:
        return self.maze.get()

    def visualize(self) -> None:
        for row in self.maze.get():
            print(' '.join(row))


def generate_random_maze(
        height: int = 10, wide: int = 10, num_wall: int = 20
    ) -> Maze:
    if height < 1 or wide < 1:
        raise Exception('Height or Wide is not available')
    maze_list = [['.' for _ in range(wide)] for _ in range(height)]
    for ith in range(num_wall):
        row = random.randint(0, height-1)
        col = random.randint(0, wide-1)
        maze_list[row][col] = 'x'
    start_point = [random.randint(0, height-1), random.randint(0, wide-1)]
    while maze_list[start_point[0]][start_point[1]] != '.':
        start_point = [random.randint(0, height-1), random.randint(0, wide-1)]
    end_point = [random.randint(0, height-1), random.randint(0, wide-1)]
    while maze_list[end_point[0]][end_point[1]] != '.':
        end_point = [random.randint(0, height-1), random.randint(0, wide-1)]
    maze_list[start_point[0]][start_point[1]] = 'o'
    maze_list[end_point[0]][end_point[1]] = '0'
    return Maze(maze=maze_list)
