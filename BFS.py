from collections import deque

class Graph:
    def __init__(self):
        self.graph={}

    def add_edge(self,u,v):
        if u not in self.graph:
            self.graph[u]=[]
        self.graph[u].append(v)

        if v not in self.graph:
            self.graph[v]=[]
        self.graph[v].append(u)

    def bfs_traversal(self,start):
        visited=set()
        queue=deque([start])
        visited.add(start)

        while queue:
            vertex=queue.pop()
            print(vertex, end=" ")
        
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
graph=Graph()

graph.add_edge(1,2)
graph.add_edge(1,3)
graph.add_edge(2,4)
graph.add_edge(2,5)
graph.add_edge(3,6)
graph.add_edge(3,7)

print("Bfs traversal:")
graph.bfs_traversal(7)
