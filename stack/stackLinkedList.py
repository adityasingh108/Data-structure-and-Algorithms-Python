class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next
class Stack:
    def __init__(self):
        self.linked_list = LinkedList()
        
    def __str__(self):
        '''Return the elemens of stack'''
        values = [str(x.value) for x in self.linked_list]
        return '\n'.join(values)    
    
    def isEmpty(self):
        '''This method check whether the stack is empty or not'''
        if self.linked_list.head == None:
            return True 
        else:
            return False
    def push(self,value):
        '''This method insert the value in the linked list in the stack'''
        node = Node(value)
        node.next = self.linked_list.head
        self.linked_list.head =node
    def pop(self):
        '''This method delete the elements in Firist in Firist Order'''
        if self.isEmpty():
            return 'The Stack is empty'
        else:
            node_value = self.linked_list.head.value
            self.linked_list.head = self.linked_list.head.next
            return node_value                        
    def peek(self):
        '''This method Retrive the elements in Firist in Firist Order'''
        if self.isEmpty():
            return 'The Stack is empty'
        else:
            node_value = self.linked_list.head.value
            return node_value       
    def delete(self):
        self.linked_list.head = None
        
        
CustomStack = Stack()
CustomStack.push(1)        
CustomStack.push(2)        
CustomStack.push(3)        
CustomStack.push(4)        
CustomStack.push(5)
print(CustomStack)        
                 