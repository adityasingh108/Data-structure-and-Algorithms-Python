# Questions : Given a directed Graph  and two nodes write an algorithms to wheher tree  is route from one node to another
class Graph:
    def __init__(self,gdict = None):
       if gdict is None:
           gdict = {}
       self.gdict = gdict
       
    def addEdge(self,vertex,edge):
        self.gdict[vertex].append(edge) 
        
    def checkRoute(self,startNode,endNode):
        visited = [startNode]      
        queue = [startNode] 
        path = False
        while queue:
            devrertex = queue.pop(0)
            for adjecentVertex in self.gdict[devrertex]:
                if adjecentVertex not in visited:
                    if adjecentVertex == endNode:
                        path = True
                        break
                    else:
                        visited.append(adjecentVertex) 
                        queue.append(adjecentVertex)     
        return path
    
    
customDict = {
    "a":['c','d','b'],
    "b":['j'],
    "c":['g'],
    "d":[],
    "e":['f','a'],
    "f":['i'],
    "g":['d','h'],
    "h":[],
    "i":[],
    "j":[]
}    
    
   
g = Graph(customDict)
print(g.checkRoute("a",'e'))    
                        