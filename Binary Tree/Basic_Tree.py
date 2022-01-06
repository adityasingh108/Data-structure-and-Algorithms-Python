class TreeNode:
    def __init__(self,data,children= []):
        self.data = data
        self.children = children
    def __str__(self,level=0):
        ret = " " *level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret
    def addChild(self,TreeNode):
        self.children.append(TreeNode)
        
        
# creating A tree root                
tree = TreeNode('Drinks',[])
hot = TreeNode('hot',[])
cold = TreeNode('cold',[])
tree.addChild(hot)
tree.addChild(cold)
# print(tree)
tea = TreeNode('Tea',[])
cofee = TreeNode('cofee',[])
fanta = TreeNode('fanta',[])
cola = TreeNode('cola',[])
hot.addChild(tea)
hot.addChild(cofee)
cold.addChild(cola)
cold.addChild(fanta)
print(tree)