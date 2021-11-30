# step 2 create a node to assign a value and refreence to null  
class Node:
    def __init__(self ,value=None):
        self.value=value
        self.next = None


# step 1 create a head and tail to assign a value None      

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None        
# priting the linked list 
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node =node.next
# Insertion of singlyLinkedList
    def insertSLL(self,value,location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location-1:
                    tempNode=tempNode.next
                    index +=1
                nextNode = tempNode.next
                tempNode.next = newNode
                tempNode.next = nextNode     
    # singly Linked List Transversal             
    def transversal(self):
        if self.head is None:
            print('The SLL does not exist')
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next  
 ##   singly Linked List serching the node value                                                  
    def searchSLL(self, nodeValue):
        if self.head is None:
           return "The list does not exist"
        else:
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                    return node.value
                node = node.next
            return "The value does not exist in this list"
        
## deleting the node 
    def deleteNode(self,location):
        if self.head is None:
            return "singly Linked List not found" 
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while  index < location-1:
                    tempNode = tempNode.next
                    index +=1
                nextNode = tempNode.next
                tempNode.next = nextNode.next  
                
## detete the Entire Singly sinked lIst
    def deleteEntireSLL(self):
        if self.head is None:
            return "singly Linked List not found" 
        else:
            self.head = None
            self.tail = None    
                                           
                                   
            
                
                    
# create a linked list using these class  

SinglyLinkedList = SLinkedList()
SinglyLinkedList.insertSLL(1,0)
SinglyLinkedList.insertSLL(1,0)


# case 1 at the begning of the linked list   

SinglyLinkedList.insertSLL(5,0)

# case 2 at the middle of the linked list  
SinglyLinkedList.insertSLL(10,1)
SinglyLinkedList.insertSLL(50,0)
SinglyLinkedList.deleteEntireSLL()

print([node.value for node in SinglyLinkedList])




       
                