# disjoint set in python
class Disjoint:
    def __init__(self,vertices):
        self.vertices = vertices
        self.parent = {}
        for v in vertices:
            self.parent[v]=v
        self.rank = dict.fromkeys(vertices,0)
    def find(self,item):
        if self.parent[item]==item:
            return item
        else:
            return self.find(self.parent[item])
    def union(self,x,y):
        x_root = self.find(x)         
        y_root = self.find(y) 
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] =y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root]=x_root
        else:
            self.parent[x_root] =y_root
            self.rank[x_root] = +1

vertices = ['A','B','C','D','E']
disjoint = Disjoint(vertices)
disjoint.union("A","B")                           
disjoint.union("A","C")                           
print(disjoint.find('A'))
            