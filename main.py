from src import maze

maze_list = [['o', 'x', '.', '.', '.', '.', '.', '.'],
             ['.', 'x', '.', 'x', 'x', 'x', 'x', '.'],
             ['.', 'x', '.', 'x', '.', '.', '.', '.'],
             ['.', '.', '.', 'x', '.', 'x', 'x', 'x'],
             ['x', 'x', '.', '.', '.', '.', '.', '.'],
             ['x', '.', '.', 'x', '.', 'x', 'x', '.'],
             ['.', '.', 'x', '.', '.', 'x', '0', '.']]

a_maze = maze.Maze(maze=maze_list)
# a_maze = maze.generate_random_maze()
a_maze.visualize()