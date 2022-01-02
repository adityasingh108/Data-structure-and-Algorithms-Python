# Question 2: Implement an algorithms to find the nth last element og the linked list

from LinkedList import LinkedList

def ReturnKthToLast(li, n):
    pointer1 = li.head
    pointer2 = li.head
    for i in range(n):
        if pointer2 is None:
            return None
        pointer2 = pointer2.next
    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1


li = LinkedList()
print(li.generate(10, 0, 20))
print(ReturnKthToLast(li, 3))
