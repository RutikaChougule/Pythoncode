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
    
    def dfs(self,v,visited):
        visited.add(v)
        print(v,end="")
 
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.dfs(neighbor,visited)
    def dfs_traversal(self):
        visited=set()
        for vertex in self.graph:
            if vertex not in visited:
                self.dfs(vertex, visited)
graph=Graph()

graph.add_edge(1,2)
graph.add_edge(1,3)
graph.add_edge(2,4)
graph.add_edge(2,5)
graph.add_edge(3,6)
graph.add_edge(3,7)

print("\n DFS Travesal:",end=" ")
graph.dfs_traversal()


        