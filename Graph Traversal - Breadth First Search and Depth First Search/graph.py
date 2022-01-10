class Graph:
    def __init__(self,gdict = None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict  
    def addEdge(self,vertex,edge):
        self.gdict[vertex].append(edge)
        
    def bfs(self,vertex):
        visited = [vertex]
        queue = [vertex]
        while queue:
            deVertex = queue.pop(0)
            print(deVertex)
            for adjecentVertex in self.gdict[deVertex]:
                if adjecentVertex not in visited:
                    visited.append(adjecentVertex)
                    queue.append(adjecentVertex)
                    
                    
    def dfs(self,vertex):
        visited = [vertex]
        stack = [vertex]
        while stack:
            popValue =stack.pop()
            print(popValue)
            for adjecentVertex in self.gdict[popValue]:
                if adjecentVertex not in visited:
                    visited.append(adjecentVertex)
                    stack.append(adjecentVertex)
                    

                          

customDict = { "a" : ["b","c"],
            "b" : ["a", "d", "e"],
            "c" : ["a", "e"],
            "d" : ["b", "e", "f"],
            "e" : ["d", "f", "c"],
            "f" : ["d", "e"]
               }            
CustomGraph = Graph(customDict)
CustomGraph.dfs("a")
