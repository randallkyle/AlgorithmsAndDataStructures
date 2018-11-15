import math

def treeDepth(node):
    if (node==None)
        return -1
    leftDepth=treeDepth(node.left) + 1
    rightDepth = treeDepth(node.right) + 1
    return (math.max(leftDepth,rightDepth))

def isBalanced(tree):
    current=tree.head
    # pre post or inline order
    #breadth depth or
    leftDepth=treeDepth(current.left)
    rightDepth=treeDepth(current.right)

    return (math.abs(leftDepth - rightDepth)==0)


'''

Change this to instead of getting the depth and then comparing, maybe just worrying about the current level?

'''
