# solve fibonacci sries using dyanmic programming


# Top down method

def fibonacciTopDown(n, memo):
    if n < 0:
        return 'Use only positive values'
    if n == 1:
        return 0

    if n == 2:
        return 1

    if not n in memo:
        memo[n] = fibonacciTopDown(n-1, memo) + fibonacciTopDown(n-2, memo)
    return memo[n]


myDIct = {}
print(fibonacciTopDown(5, myDIct))

# Botom up  Tabulation

def fibonacciBottomUp(n):
    table = [0, 1]
    for i in range(2, n+1):
        table.append(table[i-1]+table[i-2])
    return table[n-1]


print(fibonacciBottomUp(5))
