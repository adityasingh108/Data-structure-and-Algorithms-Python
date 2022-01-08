# Questtons 3 : write code t the partition of linked list arround a  value of x :
#              such that all nodes less than x came before all nodes greater than or eqal to x              

from LinkedList import LinkedList       

def partition(ll,x):
    ''' this method patition the linked list x such tha graeter node is left side and smaller node is right side'''
    current_node = ll.head
    ll.tail = ll.head
    while  current_node:
        next_node = current_node.next
        current_node.next = None
        if current_node.value < x:
            current_node.next = ll.head
            ll.head = current_node
        else:
            ll.tail.next = current_node
            ll.tail = current_node
        current_node = next_node

CustomLL = LinkedList()
CustomLL.generate(12,0,12)                
print(CustomLL)
partition(CustomLL,4)
print(CustomLL)

            
            