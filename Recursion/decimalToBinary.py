# Question :- convert the decimal number to binary number using recursion 

# step 1 : Recursive flow :
#     f(n) = n mod 2 + 10 * f(n/2)
    
# step 2 : Base case:
#     0 return 0
    
# step 3 : intenssional case 
#     1.5
#     -1.5        


def decimalToBinay(n):
    ''' Decimal to Binary'''
    assert int(n) == n,'Number should be integer only'
    if n==0:
        return 0
    else:
        return n %2 + 10 * decimalToBinay(int(n/2)) 
    
print(decimalToBinay(12))    
    