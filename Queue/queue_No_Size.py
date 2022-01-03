class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        ''' PRint the item in console '''
        value = [str(x) for x in self.items]
        return ' '.join(value)

    def isEmpty(self):
        '''Check Whether a Queue is Empty or not'''
        if self.items == []:
            return True
        else:
            return False

    def enQueue(self, value):
        '''This method insert the element  in the Queue'''
        self.items.append(value)
        return "The element is inserted at the end of Queue"

    def deQueue(self):
        '''delete the elements at the last in the way of FIFO'''
        if self.isEmpty():
            return 'There is no elements in the Queue to deQueue'
        else:
            return self.items.pop(0)

    def peek(self):
        '''Retrieve the elements at the last in the way of FIFO'''
        if self.isEmpty():
            return 'There is no elements in the Queue to deQueue'
        else:
            return self.items(0)

    def delete(self):
        '''Delete the all Queue'''
        self.items = None


customQueue = Queue()
print(customQueue.isEmpty())
customQueue.enQueue(1)
customQueue.enQueue(2)
customQueue.enQueue(3)
customQueue.enQueue(4)
customQueue.enQueue(4)
print(customQueue)
print('----------------')
customQueue.deQueue()
print(customQueue)
