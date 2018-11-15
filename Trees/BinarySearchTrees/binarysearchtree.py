from treenode import TreeNode
import sys

class BinarySearchTree:
    
    @staticmethod
    def isBinarySearchTree(tree):
        '''Returns True if tree is a valid binary search tree, otherwise false'''

        # empty trees are valid
        #if tree==None or tree.value==None:
        #    return True

        #else:
        # get the largest possible value
        maxVal = sys.maxsize

        # get the smallest possible value
        minVal = -1*sys.maxsize

        # returns false if it finds and invalid node, otherwise true
        return BinarySearchTree.isBST(tree, minVal, maxVal)
        
    @staticmethod
    def isBST(node, minVal, maxVal):
        ''' Recursively checks for invalid nodes, returns false if any are found '''

        # Empty nodes are valid
        if node == None:
            return True

        #if the node is outside the range of the lowest and highest observed values
        if node.value <= minVal or node.value > maxVal:
            return False

        # otherwise recursively call to the left and right with new min/max values
        else:
            return(BinarySearchTree.isBST(node.left, minVal, node.value) and BinarySearchTree.isBST(node.right, node.value, maxVal))
