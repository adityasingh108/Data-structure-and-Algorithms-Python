class heap:
    def __init__(self,size):
        self.customList = (size+1) *[None]
        self.heapSize = 0
        self.maxSize = size +1
        
def peekHeap(rootNode):
    if not rootNode:
        return
    return rootNode.customList[1]

def sizeHeap(rootNode):
    if not rootNode:
        return
    return rootNode.heapSize


def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    for i in range(1, rootNode.heapSize+1):
        print(rootNode.customList[i])
         
def heapifyTreeInserted(rootNode,index,heapType):
    parentIndex = int(index/2)
    if index <= 1:
        return
    if heapType == "Min":
        if rootNode.customList[index] < rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] =temp
        heapifyTreeInserted(rootNode,parentIndex,heapType) 
        
    if heapType == "Max":
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] =temp
        heapifyTreeInserted(rootNode,parentIndex,heapType)

def insertNode(rootNode,nodeValue,heapType):
    if rootNode.heapSize +1 == rootNode.maxSize:
        return "The Binary Heap Tree is full" 
    else:
        rootNode.customList[rootNode.heapSize+1] = nodeValue
        rootNode.heapSize +=1
        heapifyTreeInserted(rootNode,rootNode.heapSize,heapType)
        print("The Node has been added")
        
        
def heapifyTreeExtract(rootNode, index, heapType):
    leftIndex = index * 2
    rightIndex = index * 2 + 1
    swapChild = 0

    if rootNode.heapSize < leftIndex:
        return
    elif rootNode.heapSize == leftIndex:
        if heapType == "Min":
            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
        else:
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return

    else:
        if heapType == "Min":
            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] > rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
        else:
            if rootNode.customList[leftIndex] > rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] < rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
    heapifyTreeExtract(rootNode, swapChild, heapType)
         
def extractNode(rootNode, heapType):
    if rootNode.heapSize == 0:
        return
    else:
        extractedNode = rootNode.customList[1]
        rootNode.customList[1] = rootNode.customList[rootNode.heapSize]
        rootNode.customList[rootNode.heapSize] = None
        rootNode.heapSize -= 1
        heapifyTreeExtract(rootNode, 1, heapType)
        return extractedNode
    
    
def delete(rootNode):
    rootNode.customList = None
    return "The Binary Heap Has been successfully deleted"


    
                          
    
newHeap = heap(5)
insertNode(newHeap,4,'Max')                    
insertNode(newHeap,6,'Max')                    
insertNode(newHeap,8,'Max')                    
insertNode(newHeap,10,'Max')
insertNode(newHeap,13,'Max')
print('--------LevelOrder Traversal ------')
levelOrderTraversal(newHeap)           
print('------peak  -----------------------')  
print(peekHeap(newHeap))       
print('------Size of heap  ---------------') 
print(sizeHeap(newHeap)) 
print('------ Extract ---------------------') 
print(extractNode(newHeap,'Max'))

print('------delete The Binary Heap--------') 
print(delete(newHeap))

                    





       
newBinaryHeap = heap(5)    
        