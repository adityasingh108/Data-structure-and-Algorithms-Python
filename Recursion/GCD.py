# Question :- How to find the Greatest Common Divisor (GCD) Of two number using recursion 

#  step 1 Find the recursive flow 
#    gcd (a,0) =a
#    gcd(a,b) by eculedian algorithm gcd(b ,a%b)

# step 2 find the base case (stoping case)
#       gcd(0,b)
#       gcd(a,0)
    
    
    
# step 3  unintensional case 
#     a and b should be intenger 
#     conver a and b into positive 
    
   


def gcd(a,b):
    ''' function for greatest common divisor of two number '''
    assert int(a)== a and int(b) == b ,'Intenger only'
    if a < 0:
        a = -1 *a
    if b < 0:
        b = -1 *b  
    if b ==0:
        return a
    else:
        return gcd(b,a % b)     
    
print(gcd(0 ,18))      
    