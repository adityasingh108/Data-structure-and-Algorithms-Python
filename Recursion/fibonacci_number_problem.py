# Question : Find the Fibonacci series series using recursion 


# step 1 Recusive flow 
#     f(n) = (n-1) + (n-2)
    
# step 2  base case  
#     0 and 1  return 0 nad 1
    
# step 3 unintensional case 
#     number should be greter than 0 and integer only    

def Fibonacci(n):
    ''' Find a fibonacci number using Recursion'''
    assert n >=0 and int(n) == n,'Fibonacci number only be positive numbers'
    if n in [0,1]:
        return n 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
    
    
print(Fibonacci(7)) 