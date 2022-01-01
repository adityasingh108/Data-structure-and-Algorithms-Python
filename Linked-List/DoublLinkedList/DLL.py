class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class doublyLinkedList:
    def __init(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def createDLL(self, nodeValue):
        '''create a singly Linked List'''
        node = Node(nodeValue)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        return 'The doubly linked list is created'

    def insertDLL(self, nodeValue, location):
        ''' insert the node in the doubly linked list '''
        if self.head is None:
            print('The Doubly Linked List Is not Present')
        else:
            new_node = Node(nodeValue)
            if location == 0:
                new_node.prev = None
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            elif location == 1:
                new_node.next = None
                new_node.prev = self.tail
                self.tail.next = new_node
                self.tail = new_node
            else:
                temp_node = self.head
                index = 0
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1
                new_node.next = temp_node.next
                new_node.prev = temp_node
                new_node.next.prev = new_node
                temp_node.next = new_node

    def traversalDLL(self):
        '''Traverse the dobly Linked list '''
        if self.head is None:
            print('The Linked is not present')
        else:
            temp_node = self.head
            while temp_node:
                print(temp_node.value)
                temp_node = temp_node.next

    def reverseDLL(self):
        ''' traverse the doubly linked list in the reverse'''
        if self.head is None:
            print('Linked list is not present')
        else:
            temp_node = self.tail
            while temp_node:
                print(temp_node.value)
                temp_node = temp_node.prev

    def serchDLL(self, nodeValue):
        '''this method serch the node value and retun the node'''
        if self.head is None:
            print("There is not any linked list to present")
        else:
            temp_node = self.head
            while temp_node:
                if temp_node.value == nodeValue:
                    return temp_node.value
                else:
                    temp_node = temp_node.next
            return "The node is does not exist in the Doubly Linked List "

    def deletionNode(self, location):
        ''' This method delete the Node as per the user input '''
        if self.head is None:
            print('There is No DLL present')
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                current_node = self.head
                index = 0
                while current_node < location - 1:
                    current_node = current_node.next
                    index += 1
                current_node.next = current_node.next.next
                current_node.next.prev = current_node
            print('The node has been uccesfully deleted')

    def deletionDDL(self):
        '''Delete the entir eDoubly Linked List'''
        if self.head is None:
            print('There is not DLL persistent')
        else:
            temp_node = self.head
            while temp_node:
                temp_node.prev = None
                temp_node = temp_node.next
            self.head = None
            self.tail = None
        print('The deletion of DDl is completed ')


doublyLL = doublyLinkedList()
print('---------------------Creation-------')
doublyLL.createDLL(1)
print([node.value for node in doublyLL])
# insert he node in the at the begning
print('---------------------insert at the Begning-------')
doublyLL.insertDLL(1, 0)
print([node.value for node in doublyLL])
# insert the node in the last position
print('---------------------insert at the last Postion -------')
doublyLL.insertDLL(2, 1)
print([node.value for node in doublyLL])
# insert the node at the specific position
print('---------------------insert at the specif position-------')
doublyLL.insertDLL(3, 2)
doublyLL.insertDLL(4, 3)
print([node.value for node in doublyLL])

print('---------------------Traversal-------')
doublyLL.traversalDLL()

print('--------------------- Reverse Traversal-------')
doublyLL.reverseDLL()
print('--------------------- Serching  -------')
print(doublyLL.serchDLL(3))

print('--------------------- deelting a node   -------')
print([node.value for node in doublyLL])
doublyLL.deletionNode(1)

print('--------------------- deelting Entire Doubly Linked list   -------')

doublyLL.deletionDDL()

print([node.value for node in doublyLL])
