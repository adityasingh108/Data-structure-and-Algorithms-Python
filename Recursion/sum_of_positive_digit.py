# Question :- find the sum of digit of  positive  Numbers using Recurion 


# step 1 : recursive flow 
#     fn(n) = n mod 10 + f(n/10)
    
# step 2 base case 
#     0 return 0
    
# step 3 unintensiona case 
#     number be only positive integer only    

def sumOfDigit(n):
    ''' sum of digit of a positive number''' 
    assert n>=0 and int(n) == n ,'Positive Number only '
    if n ==0:
        return 0
    else:
        return int(n%10) + sumOfDigit(int(n/10))
    
print(sumOfDigit(6)) 