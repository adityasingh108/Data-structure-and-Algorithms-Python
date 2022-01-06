
class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        
    def __str__(self):
        return str(self.value)    

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next
class Queue:
    def __init__(self):
        self.linked_list = LinkedList()
        
    def __str__(self):
        '''Return the elemens of stack'''
        values = [str(x.value) for x in self.linked_list]
        return ' '.join(values)    
    
    def enQueue(self,value):
        new_node = Node(value)
        if self.linked_list.head == None:
            self.linked_list.head = new_node
            self.linked_list.tail = new_node
        else:
            self.linked_list.tail.next = new_node
            self.linked_list.tail = new_node
            
            
    def isEmpty(self):
        if self.linked_list.head == None:
            return True
        else:
            return False
        
    def deQueue(self):
        if self.isEmpty():
            return 'There is not any element in Queue' 
        else:
            temp_node = self.linked_list.head
            if self.linked_list.head == self.linked_list.tail:
                self.linked_list.head = None
                self.linked_list.tail = None
            else:
                 self.linked_list.head = self.linked_list.head.next
            return temp_node
        
    def peek(self):
        if self.isEmpty():
            return 'There is not any element in Queue' 
        else:
            return self.linked_list.head
        
        
    def delete(self):
        self.linked_list.head = None
        self.linked_list.tail = None    
            
 



class TreeNode:
    def __init__(self,data):
        self.data=data
        self.leftChild = None
        self.rightChild = None
    # def __str__(self,level=0):
    #     ret = " " *level + str(self.data) + "\n"
    #     # for child in self.data:
    #     #     ret += child.__str__(level+1)
    #     return ret
    
    
newBT = TreeNode('Drinks')
leftChild = TreeNode("hot")
rightChild = TreeNode("cold")
newBT.leftChild = leftChild
newBT.rightChild = rightChild

def preOrderTraversal(rootNode):
    if not rootNode:
        return 
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)
print("-------PreorderTraversal--------")    
preOrderTraversal(newBT)    
    
def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)    
print("-------InOrderTraversal--------")    
inOrderTraversal(newBT) 
def postOrderTraversal(rootNode):
    if not rootNode:
        return 
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)
    
    
print("-------PostOrderTraversal--------")    
postOrderTraversal(newBT)     
    
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
                
                
print("-------LevelOrderTraversal--------")
levelOrderTraversal(newBT)   


def searchNode(rootNode,node_value):
    if not rootNode:
        return 'The Binary Tree does not exist'
    else:
        CustomQueue = Queue()
        CustomQueue.enQueue(rootNode)
        while not(CustomQueue.isEmpty()):
            root = CustomQueue.deQueue()
            if root.value.data == node_value:
                return "Success "
            if (root.value.leftChild is not None):
                CustomQueue.enQueue(root.value.leftChild)
                
            if (root.value.rightChild is not None):
                CustomQueue.enQueue(root.value.rightChild)
        return "Not found"                    
    
                
                
print("--------------Serch A node")
print(searchNode(newBT,'cold'))      
          
def  InsertNode(rootNode,newNode):
    '''It uses  level order traversal and level order traversal always use queue '''
    if not rootNode:
        rootNode = newNode
    else:
        customQueue = Queue()
        customQueue.enQueue(rootNode)
        while  not(customQueue.isEmpty()):
            root = customQueue.deQueue()
            if root.value.leftChild is not None:
                customQueue.enQueue(root.value.leftChild)
            else:
                root.value.leftChild= newNode
                return " successfully inserted"
            
            if root.value.rightChild is not None:
                customQueue.enQueue(root.value.rightChild)
            else:
                root.value.rightChild= newNode
                return " successfully inserted"
            
           
newNode = TreeNode('cola')
print('-------------NewNode insertion --------')
print(InsertNode(newBT,newNode))
levelOrderTraversal(newBT)
            
def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        CustomQueue = Queue()
        CustomQueue.enQueue(rootNode)
        while not(CustomQueue.isEmpty()):
            root = CustomQueue.deQueue()
            
            if (root.value.leftChild is not None):
                CustomQueue.enQueue(root.value.leftChild)
                
            if (root.value.rightChild is not None):
                CustomQueue.enQueue(root.value.rightChild)
                
        DeepestNode = root.value
        return DeepestNode
    
    
deepestNode= getDeepestNode(newBT)  
print("Deepest node:",deepestNode.data) 


def deleteDeepestNode(rootNode,deepestNode):
    if not rootNode:
        return
    else:
        CustomQueue = Queue()
        CustomQueue.enQueue(rootNode)
        while  not(CustomQueue.isEmpty()):
            root = CustomQueue.deQueue()
            if root.value is deepestNode:
                root.value = None
                
            # for right child
            if root.value.rightChild:
                if root.value.rightChild is deepestNode:
                    root.value.rightChild = None
                else:
                    CustomQueue.enQueue(root.value.rightChild)
                    
            # for left child       
            if root.value.leftChild:
                if root.value.leftChild is deepestNode:
                    root.value.leftChild = None
                else:
                    CustomQueue.enQueue(root.value.leftChild)
# print('-------delete the deepest node')                    
# newNode = getDeepestNode(newBT)
# deleteDeepestNode(newBT,newNode)
# levelOrderTraversal(newBT)

def deleteNode(rootNode,node):
    if not rootNode:
        return "The binary Tree is not exist"
    else:
        CustomQueue = Queue()
        CustomQueue.enQueue(rootNode)
        while  not(CustomQueue.isEmpty()):
            root = CustomQueue.deQueue()
            
            if root.value.data == node:
                dNode= getDeepestNode(rootNode)
                root.value.data = dNode.data
                deleteDeepestNode(rootNode,dNode)
                return 'The Node has been successfully deleted'
            
            if (root.value.leftChild is not None):
                CustomQueue.enQueue(root.value.leftChild)
                
            if (root.value.rightChild is not None):
                CustomQueue.enQueue(root.value.rightChild) 
            
        return 'Failed to delete'    
    
    
    
print('-------delete the  node------')      
deleteNode(newBT,'hot')
levelOrderTraversal(newBT)



def deleteBT(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return 'The binary Tree has been successfully deleted'


print("-----Delete The whole binary Tree")
print(deleteBT(newBT))



 
            
                
                
                
        
                     
                    
                    
                    
                                                       