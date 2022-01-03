class  Queue:
    def __init__(self,max_size):
        ''' This function create the blank list and the  time complexity is O(1) and space complexity is O(n)'''
        self.items = max_size *[None]
        self.max_size = max_size
        self.start = -1
        self.top = -1
        
    def __str__(self):
        '''print the list items '''
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    def isFull(self):
        ''' This method return true if the list is full otherwise false
        Time complexity O(1) space complexity O(1)'''
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top +1 == self.max_size:
            return True
        else:
            return False
        
    def isEmpty(self):
        ''' This method return true if the list is emppty otherwise false '''
        if self.top == -1:
            return True
        else:
            return False  
        
    def enqueue(self,values):
        '''this function insert the elemet at the last '''
        if self.isFull():
            return 'The Queue is full'
        else:
            if self.top + 1 == self.max_size:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = values
            return 'The element is inserted at the end of the queue'
        
    def dequeue(self):
        '''This method delete the last elment and treturn that element'''
        if self.isEmpty():
            return 'There is not element in this Queue'
        else:
            first_element = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start +1 == self.max_size:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            return first_element   
    def peek(self):
        '''This method Retrive  the last elment and treturn that element'''
        if self.isEmpty():
            return 'There is not element in this Queue'
        else:
            return self.items[self.start]
        
        
        
    def delete(self):
        ''' delete the Queue '''
        self.items = self.max_size *[None]
        self.start = -1
        self.top = -1
        
                       
            
                         
CustomQueue = Queue(3)
CustomQueue.enqueue(1)     
CustomQueue.enqueue(1)     
CustomQueue.enqueue(1)
CustomQueue.dequeue()
CustomQueue.delete()
print(CustomQueue)     