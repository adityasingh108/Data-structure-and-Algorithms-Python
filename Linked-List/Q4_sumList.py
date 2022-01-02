# Questions 4 : you have two numbers repregented by the linked list where each node 
#               contains a single digirt,the digit are stored in the reverse order such theat the first digit  at the head of list
#               Write an functions that add the two numbers and retuen the sum of the linked list

from LinkedList import LinkedList

def SumList(llA,llB):
    ''' THis method sum the list '''
    n1 = llA.head
    n2 = llB.head
    carry = 0
    ll = LinkedList()
    while  n1 or n2:
        result  = carry
        if n1 :
            result += n1.value
            n1 = n1.next
        if n2 :
            result += n2.value
            n2 = n2.next  
        ll.add(int(result % 10))
        carry = result/10
    return ll          

    
llA = LinkedList()
llA.add(7)
llA.add(1)
llA.add(6)

llB = LinkedList()
llB.add(5)    
llB.add(9)    
llB.add(2)

print(llA)    
print(llB) 
   
print(SumList(llA,llB))   
   
            