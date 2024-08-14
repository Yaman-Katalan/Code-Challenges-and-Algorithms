# Write here the code challenge solution
class Graph:
    def __init__(self, vertices):
        self.V = vertices  # number of vertices
        self.graph = {i: [] for i in range(vertices)}  # adjacency list representation
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def dfs(self, v, visited):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs(i, visited)
    
    def transpose(self):
        g = Graph(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g
    
    def is_strongly_connected(self):
        # Step 1: DFS from the first vertex
        visited = [False] * self.V
        self.dfs(0, visited)
        
        # If DFS traversal doesn't visit all vertices, then the graph is not strongly connected
        if any(not visited_vertex for visited_vertex in visited):
            return "Not strongly connected"
        
        # Step 2: Create a transposed graph
        gr = self.transpose()
        
        # Step 3: DFS from the same vertex on the transposed graph
        visited = [False] * self.V
        gr.dfs(0, visited)
        
        # If DFS traversal on the transposed graph doesn't visit all vertices, then the graph is not strongly connected
        if any(not visited_vertex for visited_vertex in visited):
            return "Not strongly connected"
        
        return "Strongly connected"


# Example 1: Adjust if the input is 1-based
g1 = Graph(7)
edges1 = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,4],[1,7],[7,3]]
for u, v in edges1:
    g1.add_edge(u-1, v-1)  # Only adjust if input is 1-based
print(g1.is_strongly_connected())

# Example 2: No need to adjust if input is 0-based
g2 = Graph(5)
edges2 = [[1,2],[1,0],[0,4],[4,3],[3,2],[3,1],[2,1],[2,4]]
for u, v in edges2:
    g2.add_edge(u, v)  # No adjustment needed for 0-based input
print(g2.is_strongly_connected())

