class Node:
    # create a Node classs this will ceate the node  and refrence the node and the head and tail is to none 
    def __init__(self,value=None):
        self.value = value
        self.next = None
        
class circularSinglyLinkedList:
    def __init__(self):
        '''initialize the head and tail is Null '''
        self.head = None
        self.tail = None
        
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break
                   
  ## create a circular singly linked list       
    def createSLL(self,nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node 
        self.tail = node
        return 'the circular CLL has  been created'
 
  ## INSERTION OF SINGLY CIRULAR LINKED LIST 
    def insertionCirularSLL(self,value,location):
        if self.head is None:
            return 'Cirular singly linked list is not present'
        else:
            newNode = Node(value)
            if location == 0:
                # isert at the begning 
                newNode.next = self.head
                self.head= newNode
                self.tail.next = newNode
            elif location == 1:
                # insert at the last
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode    
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index +=1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
            return "The circular singly linked list has been inserted"  
        
# Cirular singly linked list transversal 
    def traversalCSLL(self):
        if self.head is None:
            return 'Linked List is empty'
        else:
            tempNode = self.head
            while tempNode :
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    break                  
        
# serching the element in the  circular linked list  
    def serchCircularSLL(self,nodeValue):
        if self.head is None:
            return 'Circular singly Linked list is not present'
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                        return tempNode.value
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    return "The Node is does not exist "    
                       
# deletion a node in circular singly linked list 
    def deleteNode(self,location):
        if self.head is None:
            print('Ther is not node in the circular singly linked list')
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = self.head
                    self.tail = node        
            else:
                tempNode = self.head 
                index = 0 
                while  index < location -1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next =  nextNode.next
# delete the entire circular singly linked list                 
    def deleteEntireCSLL(self):
        self.head = None
        self.tail.next = None
        self.tail = None                       
                                                       

            
        
circularSLL = circularSinglyLinkedList()
print(circularSLL.createSLL(1))
circularSLL.insertionCirularSLL(0,0)
circularSLL.insertionCirularSLL(12,1)
circularSLL.insertionCirularSLL(555,2)
circularSLL.insertionCirularSLL(6,3)
circularSLL.insertionCirularSLL(65,4)
circularSLL.insertionCirularSLL(564,5)
circularSLL.insertionCirularSLL(87,6)
circularSLL.insertionCirularSLL(54,7)
circularSLL.insertionCirularSLL(58,8)
circularSLL.insertionCirularSLL(78,9)
# circularSLL.traversalCSLL()
print([node.value for node in circularSLL])
# deleion of node at the begning 
circularSLL.deleteNode(0)

# deleting the node at the last ? 
circularSLL.deleteNode(1)
circularSLL.deleteEntireCSLL()



print([node.value for node in circularSLL])
        