# solve House robber problem robber cannt stole the adjecnt house




def houseRobber(house,currentHouse):
    if currentHouse >= len(house):
        return 0
    
    else:
        steal_first = house[currentHouse] + houseRobber(house,currentHouse +2) 
        skip_first =houseRobber(house,currentHouse +1) 
        return max(steal_first,skip_first)
    
    
    
houses = [1,5,8,9,3,5,7] 

print(houseRobber(houses,1))   
    