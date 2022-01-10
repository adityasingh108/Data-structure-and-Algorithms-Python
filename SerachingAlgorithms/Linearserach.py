def linearSearch(array,value):
    for i in range(len(array)):
        if array[i] == value:
            return i
    return -1


array =[4,56,8,2,8,3,3,6,8,6,3,3,33,6,8,89,9,3,5,6,3]  
print(linearSearch(array,50))  