# Question2 : return the minimum elemnet in the stack 


class Node:
    def __init__(self, value = None,next = None):
        self.value = value
        self.next = next
        
    def __str__(self):
        string =  str(self.value) 
        if self.next:
            string += ',' + str(self.next)
        return string    
       

class Stack:
    def __init__(self):
        self.top = None
        self.min_node = None
    
    def min(self):
        if not self.min_node:
            return None
        return self.min_node.value
    
    
    def push(self,item):
        if self.min_node and (self.min_node.value < item):
            self.min_node = Node(value = self.min_node.value,next= self.min_node)
        else:
            self.min_node  = Node(value = item,next= self.min_node)
        self.top = Node(value=item,next = self.top)
        
    def pop(self):
        if not self.top:
            return None
        self.min_node = self.min_node.next
        item = self.top.value
        self.top = self.top.next
        return item        
                
CustomStack = Stack()                
CustomStack.push(5)
print(CustomStack.min())
CustomStack.push(3)
print(CustomStack.min())