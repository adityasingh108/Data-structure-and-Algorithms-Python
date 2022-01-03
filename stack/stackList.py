class Stack:
    def __init__(self):
        self.list = []
        
    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)
    
    #Is Empty
    def isEmpty(self):
        '''Return true if the stack is empty else False'''
        if self.list == []:
            return True
        return False
    #Push
    def push(self,value):
        '''This method insert the value'''
        self.list.append(value)
        return 'The value has been successfully inserted'
    #POp
    def pop(self):
        '''This method pop the element in order to LIFO and delete the element'''
        if self.isEmpty():
            return "There is no element to pop in the stack"
        else:
            return self.list.pop()
    #peek
    def peek(self):
        '''This method return the element'''
        if self.isEmpty():
            return "There is no element to pop in the stack"
        else:
            return self.list[len(self.list)-1]
        
    #delete the entire stack    
    def deleteStack(self):
        self.list = None
        return 'The stack has been successfully deleted'
            
CustomStack = Stack()
print(CustomStack.isEmpty())
CustomStack.push(4)        
CustomStack.push(5)        
CustomStack.push(6)        
CustomStack.push(7)        
CustomStack.push(8)
print(CustomStack) 
CustomStack.pop()  
CustomStack.deleteStack()     
# print(CustomStack) 
print(CustomStack.isEmpty())