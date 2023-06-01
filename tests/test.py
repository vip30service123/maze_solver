from src import maze_interface


# maze_list = [['o', 'x', '.', '.', '.', '.', '.', '.'],
#              ['.', 'x', '.', 'x', 'x', 'x', 'x', '.'],
#              ['.', 'x', '.', 'x', '.', '.', '.', '.'],
#              ['.', '.', '.', 'x', '.', 'x', 'x', 'x'],
#              ['x', 'x', '.', '.', '.', '.', '.', '.'],
#              ['x', '.', '.', 'x', '.', 'x', 'x', '.'],
#              ['.', '.', 'x', '.', '.', 'x', '0', '.']]

# a_maze = maze.Maze(maze=maze_list)
# a_maze.update_type((6, 7), 'x')
# # a_maze = maze.generate_random_maze(height=20, wide=20, num_wall=5)
# a_maze.visualize()

# maze_solverr = maze_solver.MazeSolver(maze=a_maze)
# maze_solverr.get_shortest_path()
# print()
# for vertex in maze_solverr.get_shortest_path():
#     a_maze.change_specific_position(vertex, '_')
# a_maze.visualize()

# a_maze = maze.Maze(height=5, width=5)
# a_maze.to_list()[2][1] = 'o'
# print(a_maze.get_all_coor_from_type('.'))
# a_maze.visualize()



a_maze = maze_interface.MazeInterface()
a_maze.run()