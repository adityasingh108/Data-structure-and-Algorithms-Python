# two dimensional array minimum cost


def findMinCost(twoDarray, row, col):
    if row == -1 or col == -1:
        return float("inf")
    elif row == 0 and col == 0:
        return twoDarray[0][0]
    else:
        op1 = findMinCost(twoDarray, row-1, col)
        op2 = findMinCost(twoDarray, row, col-1)
        return twoDarray[row][col] + min(op1, op2)

TwoDList = [[4,7,8,6,4],
           [6,7,3,9,2],
           [3,8,1,2,4],
           [7,1,7,3,7],
           [2,9,8,9,3]
           ]

print(findMinCost(TwoDList,4,4))