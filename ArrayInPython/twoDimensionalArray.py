import numpy as np

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9] ])
print(twoDArray)

def serchid(array,value):
    for  i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return f" the value is at {str(i)} {str(j)}"
    return f'the value is not in the array'

print(serchid(twoDArray,45))
