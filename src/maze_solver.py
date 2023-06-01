from src.maze import Maze
from typing import List, Tuple


class MazeSolver:
    def __init__(self, maze: Maze = None) -> None:
        if maze:
            self.maze = maze
        self.all_vertices = self.retrieve_all_vertices()

    def insert_maze(self, maze: Maze) -> None:
        self.maze = maze

    def retrieve_all_vertices(self) -> List[Tuple[int, int]]:
        vertices = []
        for rowth in range(len(self.maze.to_list())):
            for colth in range(len(self.maze.to_list()[0])):
                if self.maze.to_list()[rowth][colth] == '.':
                    vertices.append((rowth, colth))
        starting_vertex = self.maze.get_starting_point()
        ending_vertex = self.maze.get_ending_point()
        return [starting_vertex] + vertices + [ending_vertex]

    def retrieve_nearby_vertices(
            self, check_vertex: Tuple[int, int], available_vertices: List[Tuple[int, int]] = None
        ) -> List[Tuple[int, int]]:
        all_possible_nearby_vertices = list(set([
            (check_vertex[0], min(check_vertex[1] + 1, len(self.maze.to_list()[0]) - 1)),
            (check_vertex[0], max(check_vertex[1] - 1, 0)),
            (min(check_vertex[0] + 1, len(self.maze.to_list())), check_vertex[1]),
            (max(check_vertex[0] - 1, 0), check_vertex[1])
        ]))
        if available_vertices:
            return [
                vertex 
                for vertex in all_possible_nearby_vertices
                if vertex in self.all_vertices and vertex != check_vertex and vertex in available_vertices
            ] 
        else:
            return [
                vertex 
                for vertex in all_possible_nearby_vertices
                if vertex in self.all_vertices and vertex != check_vertex
            ] 

    def get_shortest_path(self) -> List[Tuple[int, int]]:
        if not self.maze._is_valid_maze():
            return []

        queue = [self.all_vertices.copy()[0]]
        unvisited_vertices = self.all_vertices.copy()[1:]
        available_nearby_vertices = {}

        while queue:
            all_vertices_this_level = []
            for vertex in queue:
                nearby_vertices = self.retrieve_nearby_vertices(vertex, unvisited_vertices)
                all_vertices_this_level += nearby_vertices
                available_nearby_vertices[vertex] = nearby_vertices
            all_vertices_this_level = list(set(all_vertices_this_level))
            for vertex in queue:
                if vertex in unvisited_vertices:
                    unvisited_vertices.remove(vertex)
            queue = all_vertices_this_level
        
        shortest_path = []
        current_vertex = self.all_vertices[-1]
        try:
            while current_vertex != self.all_vertices[0]:
                for vertex, nearby_vertices in available_nearby_vertices.items():
                    if current_vertex in nearby_vertices:
                        current_vertex = vertex
                        shortest_path.append(vertex)
                        break
            return shortest_path[:len(shortest_path) - 1]
        except:
            return []
