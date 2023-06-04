import random
from typing import List, Tuple, Union


class Maze:
    def __init__(
            self, height: int = 0, width: int = 0, maze: List[List] = None
        ) -> None:
        if (height != 0 or width != 0) and maze != None:
            raise Exception("Maze is already created")

        if not maze:
            self.maze = [['.' for _ in range(width)] for _ in range(height)]
            self.height = height
            self.width = width
        else:
            self.maze = maze
            self.height = len(self.maze)
            self.width = len(self.maze[0])

    def __contains__(self, coor: Tuple[int, int]) -> bool:
        if (coor[0] < self.height 
                and coor[0] >= 0 
                and coor[1] < self.width 
                and coor[1] >= 0):
            return True
        return False

    def is_valid_maze(self) -> bool:
        '''
        Check if maze contains starting point and ending point 
        '''
        check = [0, 0]
        for row in self.maze:
            if 'o' in row:
                check[0] += 1
            if '0' in row:
                check[1] += 1
        return check == [1, 1]

    def is_starting_point_available(self) -> bool:
        for rowth in range(self.height):
            for colth in range(len(self.maze[0])):
                if self.maze[rowth][colth] == 'o':
                    return True
        return False

    def is_ending_point_available(self) -> bool:
        for rowth in range(self.height):
            for colth in range(len(self.maze[0])):
                if self.maze[rowth][colth] == '0':
                    return True
        return False

    def to_list(self) -> List:
        return self.maze

    def get_height(self) -> int:
        return self.height

    def get_width(self) -> int:
        return self.width

    def get_all_coor_from_type(self, type: str) -> List[Tuple[int, int]]:
        coor_list = []
        for rowth in range(self.height):
            for colth in range(self.width):
                if self.maze[rowth][colth] == type:
                    coor_list.append((rowth, colth))
        return coor_list

    def get_type(self, coor: Tuple[int, int]) -> str:
        return self.maze[coor[0]][coor[1]]

    def get_starting_point_coor(self) -> Tuple[int, int]:           
        for rowth in range(self.height):
            for colth in range(len(self.maze[rowth])):
                if self.maze[rowth][colth] == 'o':
                    return (rowth, colth)
        raise Exception("Missing starting point")

    def get_ending_point_coor(self) -> Tuple[int, int]:           
        for rowth in range(self.height):
            for colth in range(len(self.maze[rowth])):
                if self.maze[rowth][colth] == '0':
                    return (rowth, colth)
        raise Exception("Missing ending point")

    def update_type(self, coor: Tuple[int, int], position_type: str) -> None:
        if coor in self:
            if position_type == '.' or position_type == 'x':
                self.maze[coor[0]][coor[1]] = position_type
            elif position_type == 'o':
                if not self.is_starting_point_available():
                    self.maze[coor[0]][coor[1]] = position_type
            elif position_type == '0':
                if not self.is_ending_point_available():
                    self.maze[coor[0]][coor[1]] = position_type
            else:
                raise Exception("Undefined point type.")

    def visualize(self) -> None:
        for row in self.maze:
            print(' '.join(row))


def generate_random_maze(
        height: int = 10, width: int = 10, num_wall: int = 20
    ) -> Maze:
    if height < 1 or width < 1:
        raise Exception('Height or Width is not available')
    maze_list = [['.' for _ in range(width)] for _ in range(height)]
    for ith in range(num_wall):
        row = random.randint(0, height-1)
        col = random.randint(0, width-1)
        maze_list[row][col] = 'x'
    start_point = [random.randint(0, height-1), 
                   random.randint(0, width-1)
    ]
    while maze_list[start_point[0]][start_point[1]] != '.':
        start_point = [random.randint(0, height-1), 
                       random.randint(0, width-1)
        ]
    end_point = [random.randint(0, height-1), 
                 random.randint(0, width-1)
    ]
    while maze_list[end_point[0]][end_point[1]] != '.':
        end_point = [random.randint(0, height-1), 
                     random.randint(0, width-1)
        ]
    maze_list[start_point[0]][start_point[1]] = 'o'
    maze_list[end_point[0]][end_point[1]] = '0'
    return Maze(maze=maze_list)
