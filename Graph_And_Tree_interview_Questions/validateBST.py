# Questions : check whether this tree is Binary serach Tree or Not

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def helper(node, minVaue=float('-inf'), maxVaue=float('inf')):
    if not node:
        return True
    val = node.value
    if val <= minVaue or val >= maxVaue:
        return False
    if not helper(node.right, val, maxVaue):
        return False

    if not helper(node.left, minVaue, val):
        return False

    return True


def isValid(root):
    return helper(root)


root1 = TreeNode(7)
root1.left = TreeNode(6)
root1.right = TreeNode(8)

print(isValid(root1))
