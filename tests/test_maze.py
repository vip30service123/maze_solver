import unittest
from src import maze


class TestMaze(unittest.TestCase):
    def test_is_valid_maze(self):
        maze_list = [['o', 'x', '.', '.', '.', '.', '.', '.'],
                     ['.', 'x', '.', 'x', 'x', 'x', 'x', '.'],
                     ['.', 'x', '.', 'x', '.', '.', '.', '.'],
                     ['.', '.', '.', 'x', '.', 'x', 'x', 'x'],
                     ['x', 'x', '.', '.', '.', '.', '.', '.'],
                     ['x', '.', '.', 'x', '.', 'x', 'x', '.'],
                     ['.', '.', 'x', '.', '.', 'x', '0', '.']]
        test_maze = maze.Maze(maze=maze_list)
        self.assertTrue(test_maze.is_valid_maze())

        maze_list = [['o', 'x', '.', '.', '.', '.', '.', '.'],
                     ['o', 'x', '.', 'x', 'x', 'x', 'x', '.'],
                     ['.', 'x', '.', 'x', '.', '.', '.', '.'],
                     ['.', '.', '.', 'x', '.', 'x', 'x', 'x'],
                     ['x', 'x', '.', '.', '.', '.', '.', '.'],
                     ['x', '.', '.', 'x', '.', 'x', 'x', '.'],
                     ['.', '.', 'x', '.', '.', 'x', '0', '.']]
        test_maze = maze.Maze(maze=maze_list)
        self.assertFalse(test_maze.is_valid_maze())

        maze_list = [['', 'x', '.', '.', '.', '.', '.', '.'],
                     ['', 'x', '.', 'x', 'x', 'x', 'x', '.'],
                     ['.', 'x', '.', 'x', '.', '.', '.', '.'],
                     ['.', '.', '.', 'x', '.', 'x', 'x', 'x'],
                     ['x', 'x', '.', '.', '.', '.', '.', '.'],
                     ['x', '.', '.', 'x', '.', 'x', 'x', '.'],
                     ['.', '.', 'x', '.', '.', 'x', '0', '.']]
        test_maze = maze.Maze(maze=maze_list)
        self.assertFalse(test_maze.is_valid_maze())

        maze_list = [['o', 'x', '.', '.', '.', '.', '.', '.'],
                     ['0', 'x', '.', 'x', 'x', 'x', 'x', '.'],
                     ['.', 'x', '.', 'x', '.', '.', '.', '.'],
                     ['.', '.', '.', 'x', '.', 'x', 'x', 'x'],
                     ['x', 'x', '.', '.', '.', '.', '.', '.'],
                     ['x', '.', '.', 'x', '.', 'x', 'x', '.'],
                     ['.', '.', 'x', '.', '.', 'x', '0', '.']]
        test_maze = maze.Maze(maze=maze_list)
        self.assertFalse(test_maze.is_valid_maze())

        maze_list = [['o', 'x', '.', '.', '.', '.', '.', '.'],
                     ['.', 'x', '.', 'x', 'x', 'x', 'x', '.'],
                     ['.', 'x', '.', 'x', '.', '.', '.', '.'],
                     ['.', '.', '.', 'x', '.', 'x', 'x', 'x'],
                     ['x', 'x', '.', '.', '.', '.', '.', '.'],
                     ['x', '.', '.', 'x', '.', 'x', 'x', '.'],
                     ['.', '.', 'x', '.', '.', 'x', '.', '.']]
        test_maze = maze.Maze(maze=maze_list)
        self.assertFalse(test_maze.is_valid_maze())

    def test_is_starting_point_available(self):
        maze_list = [['o', 'x', '.', '.', '.', '.', '.', '.'],
                     ['.', 'x', '.', 'x', 'x', 'x', 'x', '.'],
                     ['.', 'x', '.', 'x', '.', '.', '.', '.'],
                     ['.', '.', '.', 'x', '.', 'x', 'x', 'x'],
                     ['x', 'x', '.', '.', '.', '.', '.', '.'],
                     ['x', '.', '.', 'x', '.', 'x', 'x', '.'],
                     ['.', '.', 'x', '.', '.', 'x', '0', '.']]
        test_maze = maze.Maze(maze=maze_list)
        self.assertTrue(test_maze.is_starting_point_available())

        maze_list = [['.', 'x', '.', '.', '.', '.', '.', '.'],
                     ['.', 'x', '.', 'x', 'x', 'x', 'x', '.'],
                     ['.', 'x', '.', 'x', '.', '.', '.', '.'],
                     ['.', '.', '.', 'x', '.', 'x', 'x', 'x'],
                     ['x', 'x', '.', '.', '.', '.', '.', '.'],
                     ['x', '.', '.', 'x', '.', 'x', 'x', '.'],
                     ['.', '.', 'x', '.', '.', 'x', '0', '.']]
        test_maze = maze.Maze(maze=maze_list)
        self.assertFalse(test_maze.is_starting_point_available())

    def test_is_ending_point_available(self):
        maze_list = [['o', 'x', '.', '.', '.', '.', '.', '.'],
                     ['.', 'x', '.', 'x', 'x', 'x', 'x', '.'],
                     ['.', 'x', '.', 'x', '.', '.', '.', '.'],
                     ['.', '.', '.', 'x', '.', 'x', 'x', 'x'],
                     ['x', 'x', '.', '.', '.', '.', '.', '.'],
                     ['x', '.', '.', 'x', '.', 'x', 'x', '.'],
                     ['.', '.', 'x', '.', '.', 'x', '0', '.']]
        test_maze = maze.Maze(maze=maze_list)
        self.assertTrue(test_maze.is_ending_point_available()())

        maze_list = [['o', 'x', '.', '.', '.', '.', '.', '.'],
                     ['.', 'x', '.', 'x', 'x', 'x', 'x', '.'],
                     ['.', 'x', '.', 'x', '.', '.', '.', '.'],
                     ['.', '.', '.', 'x', '.', 'x', 'x', 'x'],
                     ['x', 'x', '.', '.', '.', '.', '.', '.'],
                     ['x', '.', '.', 'x', '.', 'x', 'x', '.'],
                     ['.', '.', 'x', '.', '.', 'x', '.', '.']]
        test_maze = maze.Maze(maze=maze_list)
        self.assertFalse(test_maze.is_ending_point_available()())

    def test_to_list(self):
        maze_list = [['o', 'x', '.', '.', '.', '.', '.', '.'],
                     ['.', 'x', '.', 'x', 'x', 'x', 'x', '.'],
                     ['.', 'x', '.', 'x', '.', '.', '.', '.'],
                     ['.', '.', '.', 'x', '.', 'x', 'x', 'x'],
                     ['x', 'x', '.', '.', '.', '.', '.', '.'],
                     ['x', '.', '.', 'x', '.', 'x', 'x', '.'],
                     ['.', '.', 'x', '.', '.', 'x', '0', '.']]
        test_maze = maze.Maze(maze=maze_list)
        self.assertEqual(test_maze.to_list(), maze_list)

    def test_get_height(self):
        maze_list = [['o', 'x', '.', '.', '.', '.', '.', '.'],
                     ['.', 'x', '.', 'x', 'x', 'x', 'x', '.'],
                     ['.', 'x', '.', 'x', '.', '.', '.', '.'],
                     ['.', '.', '.', 'x', '.', 'x', 'x', 'x'],
                     ['x', 'x', '.', '.', '.', '.', '.', '.'],
                     ['x', '.', '.', 'x', '.', 'x', 'x', '.'],
                     ['.', '.', 'x', '.', '.', 'x', '0', '.']]
        test_maze = maze.Maze(maze=maze_list)
        self.assertEqual(test_maze.get_height(), len(maze_list))

    def test_get_width(self):
        maze_list = [['o', 'x', '.', '.', '.', '.', '.', '.'],
                     ['.', 'x', '.', 'x', 'x', 'x', 'x', '.'],
                     ['.', 'x', '.', 'x', '.', '.', '.', '.'],
                     ['.', '.', '.', 'x', '.', 'x', 'x', 'x'],
                     ['x', 'x', '.', '.', '.', '.', '.', '.'],
                     ['x', '.', '.', 'x', '.', 'x', 'x', '.'],
                     ['.', '.', 'x', '.', '.', 'x', '0', '.']]
        test_maze = maze.Maze(maze=maze_list)
        self.assertEqual(test_maze.get_width(), len(maze_list[0]))

    def test_get_all_coor_from_type(self):
        maze_list = [['o', 'x', '.', '.', '.', '.', '.', '.'],
                     ['.', 'x', '.', 'x', 'x', 'x', 'x', '.'],
                     ['.', 'x', '.', 'x', '.', '.', '.', '.'],
                     ['.', '.', '.', 'x', '.', 'x', 'x', 'x'],
                     ['x', 'x', '.', '.', '.', '.', '.', '.'],
                     ['x', '.', '.', 'x', '.', 'x', 'x', '.'],
                     ['.', '.', 'x', '.', '.', 'x', '0', '.']]
        test_maze = maze.Maze(maze=maze_list)
        x_type_coors = [(0, 1), (1, 1), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (3, 3), (3, 5), (3, 6), (3, 7), (4, 0), (4, 
1), (5, 0), (5, 3), (5, 5), (5, 6), (6, 2), (6, 5)]
        dot_type_coors = [(0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (1, 0), (1, 2), (1, 7), (2, 0), (2, 2), (2, 4), (2, 5), (2, 
6), (2, 7), (3, 0), (3, 1), (3, 2), (3, 4), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (5, 1), (5, 2), (5, 4), (5, 7), (6, 0), (6, 1), (6, 3), (6, 4), (6, 7)]
        start_type_coors = [(0, 0)]
        end_type_coors = [(6, 7)]
        self.assertEqual(test_maze.get_all_coor_from_type('x'), x_type_coors)
        self.assertEqual(test_maze.get_all_coor_from_type('.'), dot_type_coors)
        self.assertEqual(test_maze.get_all_coor_from_type('o'), start_type_coors)
        self.assertEqual(test_maze.get_all_coor_from_type('0'), end_type_coors)

    def test_get_type(self):
        pass

    def test_get_ending_point_coor(self):
        pass

    def test_update_type(self):
        pass

    def test_generate_random_maze(self):
        pass




if __name__ == '__main__':
    unittest.main()