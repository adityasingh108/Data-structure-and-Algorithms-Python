class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = []
        self.nodes = []

    def addEdge(self, s, d, w):
        self.graph.append([s, d, w])

    def addNode(self, value):
        self.nodes.append(value)

    def print_solution(self, dist):
        print('Vertex distances from source')
        for key, value in dist.items():
            print('  ' + key, ':   ', value)

    def bellmanFord(self,src):
        dist = {i:float("infinity") for i in self.nodes}
        dist[src] = 0
        
        for _ in range(self.v-1):
            for s,d,w in self.graph:
                if dist[s] != float("infinity") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] +w
                    
        
        for s,d,w in self.graph:
                if dist[s] != float("infinity") and dist[s] + w < dist[d]:
                    print('graph cotains negative cycle')
                    return
                
        self.print_solution(dist)
        
        
g = Graph(5)
g.addNode("A")                            
g.addNode("B")                            
g.addNode("C")                            
g.addNode("D")                            
g.addNode("E")                            
g.addEdge("A", "C", 6)
g.addEdge("A", "D", 6)
g.addEdge("B", "A", 3)
g.addEdge("C", "D", 1)
g.addEdge("D", "C", 2)
g.addEdge("D", "B", 1)
g.addEdge("E", "B", 4)
g.addEdge("E", "D", 2)
g.bellmanFord("E")
                            