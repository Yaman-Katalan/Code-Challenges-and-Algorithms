from collections import deque

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, start, end):
        if start not in self.adjacency_list:
            self.adjacency_list[start] = []
        if end not in self.adjacency_list:
            self.adjacency_list[end] = []
        self.adjacency_list[start].append(end)
        self.adjacency_list[end].append(start)  # Assuming it's an undirected graph

    def breadth_first_search(self, start):
        if start not in self.adjacency_list:
            return [start]

        visited = set()
        queue = deque([start])
        result = []

        while queue:
            current_node = queue.popleft()
            if current_node not in visited:
                visited.add(current_node)
                result.append(current_node)
                for neighbor in self.adjacency_list[current_node]:
                    if neighbor not in visited:
                        queue.append(neighbor)

        return result
