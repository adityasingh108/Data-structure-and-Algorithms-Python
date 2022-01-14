# check a tree is A  balanced tree or not 

def isBalancedHelper(root):
    if root is None:
        return 0
    
    left_height = isBalancedHelper(root.left)
    if left_height == -1:
        return -1
    
    right_height = isBalancedHelper(root.right)
    if right_height == -1:
        return -1
    
    if abs(left_height-right_height) > 1:
        return -1
    
    return max(left_height,right_height) +1 
    
def isBalanced(root):
    return isBalancedHelper(root) > -1

class  Node:
    def __init__(self,value, left = None,right = None):
        self.value = value
        self.left = left
        self.right = right
        
        

N1 = Node('N1')        
N2 = Node('N2')        
N3 = Node('N3')        
N4 = Node('N4')        
N5 = Node('N5')        
N6 = Node('N6')        

N1.left = N2
N1.right = N3

N2.left = N4
N2.right = N5

N3.right = N6

print(isBalanced(N1))


        
            