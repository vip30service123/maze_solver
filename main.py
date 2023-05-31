from src import maze, maze_solver


maze_list = [['o', 'x', '.', '.', '.', '.', '.', '.'],
             ['.', 'x', '.', 'x', 'x', 'x', 'x', '.'],
             ['.', 'x', '.', 'x', '.', '.', '.', '.'],
             ['.', '.', '.', 'x', '.', 'x', 'x', 'x'],
             ['x', 'x', '.', '.', '.', '.', '.', '.'],
             ['x', '.', '.', 'x', '.', 'x', 'x', '.'],
             ['.', '.', 'x', '.', '.', 'x', '0', '.']]

# a_maze = maze.Maze(maze=maze_list)
a_maze = maze.generate_random_maze(height=20, wide=20, num_wall=5)
a_maze.visualize()

maze_solverr = maze_solver.MazeSolver(maze=a_maze)

print()
for vertex in maze_solverr.get_shortest_path():
    a_maze.change_specific_position(vertex, '_')
a_maze.visualize()

