from src.maze import Maze
from typing import List, Tuple


class MazeSolver:
    def __init__(self, maze: Maze = None) -> None:
        if maze:
            self.maze = maze
        self.all_vertices = self.retrieve_all_vertices()

    def retrieve_all_vertices(self) -> List[Tuple[int, int]]:
        vertices = []
        for rowth in range(len(self.maze.to_list())):
            for colth in range(len(self.maze.to_list()[0])):
                if self.maze.to_list()[rowth][colth] == '.':
                    vertices.append((rowth, colth))
        starting_vertex = self.maze.get_starting_point()
        ending_vertex = self.maze.get_ending_point()
        return [starting_vertex] + vertices + [ending_vertex]

    def retrieve_nearby_vertices(self, check_vertice: Tuple[int, int]) -> List[Tuple[int, int]]:
        all_possible_nearby_vertices = list(set([
            (check_vertice[0], min(check_vertice[1] + 1, len(self.maze.to_list()[0]) - 1)),
            (check_vertice[0], max(check_vertice[1] - 1, 0)),
            (min(check_vertice[0] + 1, len(self.maze.to_list())), check_vertice[1]),
            (max(check_vertice[0] - 1, 0), check_vertice[1])
        ]))
        return [
            vertice 
            for vertice in all_possible_nearby_vertices
            if vertice in self.all_vertices and vertice != check_vertice
        ] 

    def get_shortest_path(self) -> List[Tuple[int, int]]:
        queue = [self.all_vertices.copy()[0]]
        unvisited_vertices = self.all_vertices.copy()[1:]

        previous_vertex = [(-1, -1) for _ in range(len(self.all_vertices))]
        shortest_distance_from_starting_point = [len(unvisited_vertices) for _ in range(len(self.all_vertices))]
        shortest_distance_from_starting_point[0] = 0

        check_point = 0
        while queue:
            # Retrieve related vertices
            nearby_vertices = self.retrieve_nearby_vertices(queue[0])
            # Update minimum length
            minimum_distance = len(self.all_vertices)
            for nearby_vertice in nearby_vertices:
                distance = 1 + shortest_distance_from_starting_point[self.all_vertices.index(nearby_vertice)]
                if distance < minimum_distance:
                    previous_vertex[self.all_vertices.index(queue[0])] = nearby_vertice
                    shortest_distance_from_starting_point[self.all_vertices.index(queue[0])] = distance
                    minimum_distance = distance
            # Add remain vertices into queue and delete it in unvisited_vertices
            if queue[0] in unvisited_vertices:
                unvisited_vertices.remove(queue[0])
            available_nearby_vertices = []
            for vertice in nearby_vertices:
                if vertice in unvisited_vertices:
                    available_nearby_vertices.append(vertice)
            queue = queue[1:]
            queue += available_nearby_vertices
            queue = list(set(queue))

        shortest_path = []
        current_vertice = self.all_vertices[-1]
        if previous_vertex[self.all_vertices.index(current_vertice)] != (-1, -1):
            while current_vertice != self.all_vertices[0]:
                shortest_path.append(current_vertice)
                current_vertice = previous_vertex[self.all_vertices.index(current_vertice)]
            shortest_path = shortest_path[1:]
            shortest_path.reverse()
            return shortest_path
        else:
            return []