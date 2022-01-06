from queue import Queue
class BSTNode:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        
newBST = BSTNode(None)


def insertNode(rootNode,node_value):
    if rootNode.data == None:
        rootNode.data = node_value
    elif node_value <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(node_value)
        else:
            insertNode(rootNode.leftChild,node_value)
            
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(node_value)
        else:
            insertNode(rootNode.rightChild,node_value)
    return "The node has been successfully Inserted"  


def preOrderTraversal(rootNode):
    if rootNode is None:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def inorderTraversal(rootNode):
    if rootNode is None:
        return
    inorderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inorderTraversal(rootNode.rightChild)
    
def postOrderTraversal(rootNode):
    if rootNode is None:
        return
    postOrderTraversal(rootNode.leftChild)    
    postOrderTraversal(rootNode.rightChild) 
    print(rootNode.data)
    
def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        CustomQueue = Queue()
        CustomQueue.enQueue(rootNode)
        while not(CustomQueue.isEmpty()):
            root = CustomQueue.deQueue()
            print(root.value.data)
            
            if (root.value.leftChild is not None):
                CustomQueue.enQueue(root.value.leftChild)
                
            if (root.value.rightChild is not None):
                CustomQueue.enQueue(root.value.rightChild)    
                
                
def searchNode(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        print("The value is found")
    elif nodeValue < rootNode.data:
        if rootNode.leftChild.data == nodeValue:
            print("The value is found")
        else:
            searchNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild.data == nodeValue:
            print("The value is found")
        else:
            searchNode(rootNode.rightChild, nodeValue)     
            
            
def minValueNode(bstNode):
    current = bstNode
    while (current.leftChild is not None):
        current = current.leftChild
    return current

def deleteNode(rootNode, nodeValue):
    if rootNode is None:
        return rootNode
    if nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        
        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        
        temp = minValueNode(rootNode.rightChild)
        rootNode.data = temp.data 
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
    return rootNode


def delete(rootNode):
    rootNode.data = None
    rootNode.rightChild = None
    rootNode.leftChild = None
    return "The Binary Search Tree Has been deleted"
                
                                  
                   

print('------insert Node-------------') 
insertNode(newBST,10)                          
insertNode(newBST,20)                          
insertNode(newBST,25)                          
insertNode(newBST,26)                          
insertNode(newBST,30)                          
insertNode(newBST,50)                          
insertNode(newBST,60)                          
insertNode(newBST,70)

print('------preOrder Traversal---------') 
preOrderTraversal(newBST)

print('------inOrder Traversal----------')
inorderTraversal(newBST)

print('------postOrder Traversal---------')
postOrderTraversal(newBST)

print('------Level Order Traversal-------')
levelOrderTraversal(newBST)

print('------Serach Node-----------------')
searchNode(newBST,50)

                          
print('------Delete Node-----------------')
deleteNode(newBST,50)
levelOrderTraversal(newBST)

print('------Delete BSt-----------------')
print(delete(newBST))
  