#Questions 1:- Remove Dups: - write a code to remove the duplicates from an unsorted linked list
from LinkedList import  LinkedList

def remove_duplicates(li):
    if li.head is None:
        return
    else:
        current_node = li.head
        visited = set([current_node.value])
        while current_node.next:
            if current_node.next.value in visited:
                current_node.next = current_node.next.next
            else:
                visited.add(current_node.next.value)
                current_node = current_node.next
        return li
    
# write  a code that not using space buffer 
def remove_duplicates_not_using_buffer(li):
    if li.head is None:
        return     
    else:
        currentnode = li.head
        while currentnode:
            runner = currentnode
            while runner.next:
                if runner.next.value == currentnode.value:
                    runner.next = runner.next.next
                else:
                    runner=runner.next
            currentnode = currentnode.next
        return li.head
    
    
    
    
                
customLI = LinkedList()
customLI.generate(10,0,99)
print(customLI)
remove_duplicates_not_using_buffer(customLI)
print(customLI)
            
                    
                
                

        
    