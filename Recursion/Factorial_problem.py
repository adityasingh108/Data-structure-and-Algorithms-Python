# question : solve the Factorial problem  using Recursion 
# Bypass the stack memory 

# import sys
# sys.maxsize[236555]

# step 1 recusive flow 
#      f(n) = n * n-1
     
# step 2 base case 
#     0 and 1 

# step 3  unintensional case
#     not non-integer and negative number         

def factrorial(n):
    '''find a factorial  '''
    assert n>=0 and int(n) ==n ,'Factorial number only be positive numbers'
    if n in [0,1]:
        return 1
    else:
        return n* factrorial(n-1)
    
    
    
print(factrorial(12.5))