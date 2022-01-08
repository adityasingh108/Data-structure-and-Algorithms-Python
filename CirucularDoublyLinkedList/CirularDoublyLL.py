class Node:
    def __init__(self, value=None):
        '''create a blank node'''
        self.value = value
        self.next = None
        self.prev = None


class CircularDoublyLinkedList:
    def __init__(self):
        '''intiliazise head and tail None'''
        self.head = None
        self.tail = None

    def __iter__(self):
        '''Diaplay the result '''
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    def createCDLL(self, node_value):
        '''Create a node with the node value'''
        new_node = Node(node_value)
        self.head = new_node
        self.tail = new_node
        new_node.prev = new_node
        new_node.next = new_node
        return 'The Circular doubly linked list is Successfuly created'

    def insertDLL(self, nodeValue, location):
        '''This method insert the node in the Circular Doubly Linked List'''
        if self.head is None:
            print("There is Not Cirular Doubly Linked List is Exists")
        else:
            new_node = Node(nodeValue)
            if location == 0:
                new_node.next = self.head
                new_node.prev = self.tail
                self.head.prev = new_node
                self.head = new_node
                self.tail.next = new_node
            elif location == 1:
                new_node.next = self.head
                new_node.prev = self.tail
                self.head.prev = new_node
                self.tail.next = new_node
                self.tail = new_node
            else:
                temp_node = self.head
                index = 0
                while index > location-1:
                    temp_node = temp_node.next
                    index += 0
                new_node.next = temp_node.next
                new_node.prev = temp_node
                new_node.next.prev = new_node
                temp_node.next = new_node
            return "The Node has been successfully inserted"

    def searchDLL(self, nodeValue):
        '''this method sarch the node value in the Circular Doubly Linked List'''
        if self.head is None:
            print("There is not Circular linked list is Exists")
        else:
            temp_node = self.head
            while temp_node:
                if temp_node.value == nodeValue:
                    return temp_node.value
                if temp_node == self.tail:
                    return 'The node value does not exist'
                temp_node = temp_node.next

    def traversalDLL(self):
        '''This method print the node one by one'''
        if self.head is None:
            print('There is No Circular Doubly linked list is Exists')
        else:
            temp_node = self.head
            while temp_node:
                print(temp_node.value)
                if temp_node == self.tail:
                    break
                temp_node = temp_node.next

    def reverseTraversalDLL(self):
        '''This method traverse the node backward'''
        if self.head is None:
            print('There is No Circular Doubly linked list is Exists')
        else:
            temp_node = self.tail
            while temp_node:
                print(temp_node.value)
                if temp_node == self.head:
                    break
                temp_node = temp_node.prev

    def deleteNode(self, location):
        if self.head is None:
            print("There is no node in the circular Doubly linked list")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                current_node = self.head
                index = 0
                while index < location - 1:
                    current_node = current_node.next
                    index += 1
                current_node.next = current_node.next.next
                current_node.next.prev = current_node
            print('The node has been successfully deleted')

    def deleteEntireCDLL(self):
        ''' Delete the entire circular doubly linked list'''
        if self.head is None:
            print("There is no circular Doubly linked list present")
        else:
            self.tail.next = None
            temp_node = self.head
            while temp_node:
                temp_node.prev = None
                temp_node = temp_node.next
            self.head = None
            self.tail = None
            print('The circular Doubly linked list is successfully deleted')


CircularDLL = CircularDoublyLinkedList()
print("----------------Creating-----------------")
CircularDLL.createCDLL(25)
print([node.value for node in CircularDLL])

print("----------------Inserting-----------------")
CircularDLL.insertDLL(1, 0)
CircularDLL.insertDLL(2, 1)
CircularDLL.insertDLL(1, 2)
print([node.value for node in CircularDLL])

print("----------------Searching-----------------")
print(CircularDLL.searchDLL(100))

print("----------------Traversal-----------------")
CircularDLL.traversalDLL()

print("-----------Reverse Traversal--------------")
CircularDLL.reverseTraversalDLL()

print("-----------Delete Node -------------------")
CircularDLL.deleteNode(1)
print([node.value for node in CircularDLL])

print("----Delete Entire Doubly Linked list -----")
CircularDLL.deleteEntireCDLL()
print([node.value for node in CircularDLL])
