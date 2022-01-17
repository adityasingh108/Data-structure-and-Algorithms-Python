# House robber problem dyanamic programming

# top Down Memoziation

def houseRobberTD(houses, currentIndex, tempDict):
    if currentIndex >= len(houses):
        return 0
    else:
        if currentIndex not in tempDict:
            steal_first = houses[currentIndex] + \
                houseRobberTD(houses, currentIndex+2, tempDict)
            skip_first = houseRobberTD(houses, currentIndex+1, tempDict)
            tempDict[currentIndex] = max(steal_first, skip_first)

        return tempDict[currentIndex]


houses = [0, 7, 1, 30, 8, 2, 4]
print(houseRobberTD(houses, 0, {}))

# bottom up  Tabulation
def houseRobberBU(houses):
    ''' Its default check to  index 0'''
    temp_arr = [0] * (len(houses)+2)
    for i in range(len(houses)-1, -1, -1):
        temp_arr[i] = max(houses[i] + temp_arr[i+2], temp_arr[i+1])
    return temp_arr[0]

print(houseRobberBU(houses))