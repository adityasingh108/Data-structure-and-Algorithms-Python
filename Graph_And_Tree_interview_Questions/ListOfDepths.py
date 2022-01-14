# questions :- Given a BST design a algorithms  which creates a linked list of all nodes at each depth  


class linkedList:
    def __init__(self, val):
        self.val = val
        self.next = None

    def add(self, val):
        if self.next == None:
            self.next = linkedList(val)
        else:
            self.next.add(val)

    def __str__(self):
        return "({val})".format(val=self.val) + str(self.next)


class binaryTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def depth(tree):
    if tree == None:
        return 0
    if tree.left == None and tree.right == None:
        return 1
    else:
        depth_left = 1+depth(tree.left)
        depth_right = 1+depth(tree.right)
        if depth_left > depth_right:
            return depth_left
        else:
            return depth_right


def treeToLinkedList(tree, custDict={}, d=None):
    if d == None:
        d = depth(tree)
    if custDict.get(d) == None:
        custDict[d] = linkedList(tree.val)
    else:
        custDict[d].add(tree.val)
        if d == 1:
            return custDict
    if tree.left != None:
        custDict = treeToLinkedList(tree.left, custDict, d-1)
    if tree.right != None:
        custDict = treeToLinkedList(tree.right, custDict, d-1)
    return custDict


mainTree = binaryTree(1)
two = binaryTree(2)
three = binaryTree(3)
four = binaryTree(4)
five = binaryTree(5)
six = binaryTree(6)
seven = binaryTree(7)
mainTree.left = two
mainTree.right = three
two.left = four
two.right = five
three.left = six
three.right = seven

customDict = treeToLinkedList(mainTree)

for depth_level, linked_list in customDict.items():
    print("{0} {1}".format(depth_level, linked_list))
