class Stack:
    def __init__(self,max_size):
        '''Create a empty list and size '''
        self.max_size = max_size
        self.list=[]
        
    def __str__(self) -> str:
        '''This method print the value'''
        values = self.list.reverse()
        values = [str(x)for x in self.list]
        return '\n'.join(values)
    
    def isEmpty(self):
        '''This Method check whether stack is empty or not'''
        if self.list == []:
            return True
        else:
            return False
    def isFull(self):
        '''This Method check whether stack is Full or not'''
        if len(self.list) == self.max_size:
            return True
        else:
            return False
    def push(self, value):
        if self.isFull():
            return "The stack is full"
        else:
            self.list.append(value)
            return "The element has been successfully inserted"
    def pop(self):
        '''remove the elements In LIFO order'''
        if self.isEmpty():
            return 'There is no element in the stack'
        else:
            return self.list.pop() 
        
    def peek(self):
        '''retrive  the elements In LIFO order'''
        if self.isEmpty():
            return 'There is no element in the stack'
        else:
            return  self.list[len(self.list)-1]
    def deleteStack(self):
        '''Delete the Entire Stack'''
        self.list =None
        
CustomStack = Stack(4)
# print(CustomStack.isEmpty()) 
CustomStack.push(4)        
CustomStack.push(5)        
CustomStack.push(6)        
CustomStack.push(7)        
print(CustomStack.push(8))
CustomStack.push(4)        
CustomStack.push(5)        
CustomStack.push(6)        
CustomStack.push(7)        
CustomStack.push(8)                                                   
print(CustomStack)
            
    
        