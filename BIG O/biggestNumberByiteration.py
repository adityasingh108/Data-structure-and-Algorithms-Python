# Question = find the biggest number in the array and calculate the time complexity of the program  



def BiggestNumber(array):
    bigNumber = array[0]
    for index in range(1,len(array)):
        if array[index] > bigNumber:
            bigNumber = array[index]
    return bigNumber    
    
    
print(BiggestNumber([1,5,9,223,569,78,50]))        


# time complexity of the program is Big O(n) 