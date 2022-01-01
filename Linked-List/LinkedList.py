from random import randint


class Node:
    ''' This CLas Create A node '''

    def __init__(self, value=None):
        '''Create a node and assign a previous and next address is None'''
        self.value = value
        self.prev = None
        self.next = None

    def __str__(self):
        '''This method return the value of node'''
        return str(self.value)


class LinkedList:
    ''' Craete a Linked List'''

    def __init__(self, value=None):
        '''head and Tail address refreance as None'''
        self.head = None
        self.tail = None
        
    def __iter__(self):
        ''' Iterate the value and print'''
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next
        
    def __str__(self):
        '''Return a str of the Values'''
        values = [str(x.value) for x in self]
        return ' -> '.join(values)

    def __len__(self):
        '''This Method return the The Lenght of the Linked List'''
        
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result

    def add(self, value):
        '''This method add the linked list'''
        
        if self.head is None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail

    def generate(self, n, min_value, max_value):
        '''Generate the Linked List Randomly  n= number of node
        min_value = the minimum value of the node and max_num is the maximum value of the node'''
        
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(min_value, max_value))
        return self



if __name__ == '__main__':
    LinkedList = LinkedList()
    print(LinkedList.generate(12,1,12))
    print(len(LinkedList))
    print(Node(LinkedList))