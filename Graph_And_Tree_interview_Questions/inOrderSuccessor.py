# QUESTION : write an algorith, to find the next node (inorder traversa)
class Node:
    def __init__(self, key):
        self.data = key
        self.right = None
        self.left = None


def insert(node, data):
    if node is None:
        return Node(data)
    else:
        if data <= node.data:
            temp = insert(node.left, data)
            node.left = temp
            node.parent = node
        else:
            temp = insert(node.right, data)
            node.Right = temp
            node.parent = node
        return node


def minValue(node):
    current = node
    while (current is not None):
        if current.left is None:
            break
        current = current.left
    return current


def inOrderSuccessor(root, n):
    if n.right is not None:
        return minValue(n.right)
    p = n.parent
    while p is not None:
        if n != p.right:
            break
        n = p
        p = p.parent
    return p


root = None
root = insert(root, 4)
root = insert(root, 2)
root = insert(root, 8)
root = insert(root, 1)
root = insert(root, 3)
root = insert(root, 5)
root = insert(root, 9)

temp = root.left.right  # 3

succesor = inOrderSuccessor(root, temp)

if succesor is not None:
    print("Inorder successor of %d is %d" % (temp.data, succesor.data))
else:
    print('InOrder successor does not exist')
