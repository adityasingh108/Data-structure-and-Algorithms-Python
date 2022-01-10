import math

def binarySearch(array,value):
    start = 0
    end = len(array) -1
    middle = math.floor((start+end) /2)
    while not(array[middle] == value) and start <=end:
        if value < array[middle]:
            end = middle-1
        else:
            start = middle + 1 
        middle = math.floor((start+end) /2)
    if array[middle] == value:
        return middle
    else:
        return -1          
        
    
class Solution:
    def searchInsert(self,nums, target):
        start = 0
        end = len(nums) -1
        middle = math.floor((start+end) /2)
        while not(nums[middle] == target) and start <= end:
            if target < nums[middle]:
                end = middle-1
            else:
                start = middle+1
            middle = math.floor((start+end) /2)
        if nums[middle] == target:
            print(middle)
        else:
            print(middle+1)  
           
array = [1,3,5,6]  
a = Solution()
a.searchInsert(array,7)