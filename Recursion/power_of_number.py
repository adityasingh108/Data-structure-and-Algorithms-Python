# Question :- How to find the power of a positive intenger Number by the Recursion 

# base can be negative or non intenger 
# Expnonet  must be postive intenger only 

# step 1 recursive flow 
#     power = base * power(base ,exp-1)
    
# step 2 base case :
#     exp = 0 then 1
#     exp =1 the return base 
    
    
# step 3 unintensional case:
#     exp  will be greater then and it will be intenger        


def power(base ,exp):
    ''' find the power by the Recursion method'''
    assert exp >=0 and int(exp) == exp ,'The exponent must be Positive'
    if exp == 0:
        return 1
    if exp == 1:
        return base
    else:
        return base * power(base ,exp-1)
    
    
print(power(5,20)) 