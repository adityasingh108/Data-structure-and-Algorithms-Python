# Question : how to find the biggest number using recursion algorithm in the array  and find the time complexity  




def BiggestNumberRecursion(array,n):
    if n ==1:
        return array[0]
    else:
        return max(array[n-1],BiggestNumberRecursion(array,n-1))
    
    
print(BiggestNumberRecursion([1,5,9,223,569,78,50],7))
