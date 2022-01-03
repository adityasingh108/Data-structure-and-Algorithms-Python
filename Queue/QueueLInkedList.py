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
            
                       
                                    
               
CustomQueue = Queue()
CustomQueue.enQueue(1)
CustomQueue.enQueue(2)
CustomQueue.enQueue(3)
CustomQueue.enQueue(4)
print(CustomQueue)
CustomQueue.deQueue()
print(CustomQueue)
        
        
        
        
        
                    