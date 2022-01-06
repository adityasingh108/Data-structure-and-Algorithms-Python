class  binaryTree:
    def __init__(self,size):
        self.customList = size *[None]
        self.lastUsedIndex = 0
        self.maxSize = size
        
    def insertNode(self,value):
        if self.lastUsedIndex +1 == self.maxSize:
            return "The Binary  tree is full"
        self.customList[self.lastUsedIndex +1] = value
        self.lastUsedIndex +=1
        return "The Value has been successfully inserted"
    
    
    def searchNode(self,value):
        for i in range(len(self.customList)):
            if self.customList[i] == value:
                return 'Success'   
        return 'Not Found'
    
    
    def preOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        print(self.customList[index])
        self.preOrderTraversal(index*2)
        self.preOrderTraversal(index*2 + 1)
    
    
    def inOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.inOrderTraversal(index*2)
        print(self.customList[index])
        self.inOrderTraversal(index*2+1)
    
    def postOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.postOrderTraversal(index*2)
        self.postOrderTraversal(index*2+1)
        print(self.customList[index])
    
    def levelOrderTraversal(self, index):
        for i in range(index, self.lastUsedIndex+1):
            print(self.customList[i])
        
        
    def deleteNode(self,value):
        if self.lastUsedIndex  == 0:
            return 'There is no element in Binary tree to delete'
        else:
            for i in range(1,self.lastUsedIndex +1):
                if self.customList[i] == value:
                    self.customList[i] = self.customList[self.lastUsedIndex]
                    self.customList[self.lastUsedIndex]
                    return "The Node has been successfully deleted"



    def delete(self):
        self.customList = None
        return "Binary has been deleted"
                                
        
        
        
newBt = binaryTree(8)

print('--------Binary Tree using python list ------')
print('--------Inserting ------')
print(newBt.insertNode("Drinks"))
print(newBt.insertNode("Hot"))
print(newBt.insertNode("Cold"))

print('--------Search node ------')
print(newBt.searchNode("Hot"))

print('--------PreOrder Traversal ------')
newBt.preOrderTraversal(1)

print('--------InOrder Traversal ------')
newBt.inOrderTraversal(1)

print('--------postOrder Traversal ------')
newBt.postOrderTraversal(1)


print('--------LevelOrder Traversal ------')
newBt.levelOrderTraversal(1)

print('--------Delete Node ------')
print(newBt.deleteNode('Hot'))


print('--------Delete Binary Tree ------')
print(newBt.delete())




     
        
            