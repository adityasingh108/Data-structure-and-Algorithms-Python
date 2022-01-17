# number factor problem  using  dynamic programming

# TOp down memosization
def numberFactorTD(n, tempDict):
    if n in (0, 1, 2):
        return 1
    if n == 3:
        return 2
    else:
        if n not in tempDict:
            sub1 = numberFactorTD(n-1, tempDict)
            sub2 = numberFactorTD(n-3, tempDict)
            sub3 = numberFactorTD(n-4, tempDict)
            tempDict[n] = sub1 + sub2 + sub3
        return tempDict[n]


myDict = {}
print(numberFactorTD(4, myDict))


# bottom up Tabulation

def numberFactorBU(n):
    table = [1, 1, 1, 2]
    for i in range(4, n+1):
        table.append(table[i-1]+table[i-3] + table[i-4])
    return table[n]


print(numberFactorBU(4))
