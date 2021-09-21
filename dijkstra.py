class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
        self.graph.append([v, u, w])

    def minDistance(self, dist, T):
        min = float('inf')
        for v in range(self.V):
            if dist[v] < min and T[v] == False:
                min = dist[v]
                min_index = v
        return min_index

    def printSolution(self, dist):
        print("Vertice da origem")
        for node in range(self.V):
            print(node, "\t", dist[node])

    def dijkstra(self, src):
        dist = [float('inf')] * self.V
        dist[src] = 0
        T = [False] * self.V
        for count in range(self.V):
            u = self.minDistance(dist, T)
            for v in range(self.V):
                for item in self.graph:
                    if(item[0] == u) and (item[1] == v):
                        if item[2] > 0 and T[v] == False and dist[v] > dist[u] + item[2]:
                            dist[v] = dist[u] + item[2]
            T[u] = True
        self.printSolution(dist)


g = Graph(9)
g.addEdge(0, 1, 4)
g.addEdge(0, 7, 8)
g.addEdge(1, 2, 8)
g.addEdge(1, 7, 11)
g.addEdge(2, 3, 7)
g.addEdge(2, 5, 4)
g.addEdge(2, 8, 2)
g.addEdge(3, 5, 14)
g.addEdge(3, 4, 9)
g.addEdge(4, 5, 10)
g.addEdge(5, 6, 2)
g.addEdge(6, 7, 1)
g.addEdge(6, 8, 6)
g.addEdge(7, 8, 7)
g.dijkstra(0)
