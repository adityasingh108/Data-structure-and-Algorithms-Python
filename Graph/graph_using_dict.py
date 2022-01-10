class Graph:
    def __init__(self,gdict = None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict  
    def addEdge(self,vertex,edge):
        self.gdict[vertex].append(edge)

customDict = {
    'A':['b','c'],
    'B': ['a','b'],
    "C":['a','e'],
    'D':['b','e','f'],
    'E':['d','f','c'],
    'F':['d','e']    
}              

graph = Graph(customDict)
graph.addEdge('B',"e")
print(graph.gdict)