# Number factor problem using [1,3,4]

def numberFactor(n):
    if n in [0,1,2]:
        return 1
    elif n == 3:
        return 2
    else:
        subproblem1 = numberFactor(n-1)
        Subproblem2 = numberFactor(n-3)
        subproblem3 = numberFactor(n-4)
        return subproblem1+ Subproblem2+subproblem3
    



print(numberFactor(4))    