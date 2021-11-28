def searchInsert(nums, target):
        a= 0
        nums.append(target)
        nums.sort()
        for i in nums:  
            if target >=i:
                a=nums.index(i)
        
        print(nums)
        return a
    
    
print(searchInsert([1] ,0))    