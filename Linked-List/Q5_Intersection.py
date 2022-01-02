# Question : Given two Singly Linked list determines if two list intersect ,return the intersection nodes

from LinkedList import LinkedList,Node


def intersect(llA,llB):
    ''' this method intersect the common node '''
    if llA.tail is not llB.tail:
        return False
    
    lenA = len(llA)
    lenB = len(llB)
    
    shorter = llA if lenA < lenB else llB
    longer = llB if lenA < lenB else llA
    
    diff = len(longer)-len(shorter)
    
    longer_node= longer.head
    shorter_node = shorter.head
    
    for i in range(diff):
        longer_node = longer_node.next 
        
    while shorter_node is not longer_node:
        shorter_node=shorter_node.next
        longer_node=longer_node.next
        
    return longer_node    


def AddSameNode(llA,llB,value):
    '''Helper function that combine the nodes '''
    temp_node =Node(value)
    llA.tail.next = temp_node
    llA.tail = temp_node
    
    llB.tail.next = temp_node
    llB.tail = temp_node
    
llA = LinkedList()
llA.generate(5,0,5)

llB = LinkedList()
llB.generate(4,0,5)  

AddSameNode(llA,llB,11)
AddSameNode(llA,llB,14)

print(llA)
print(llB)

print(intersect(llA,llB))

  
    
    