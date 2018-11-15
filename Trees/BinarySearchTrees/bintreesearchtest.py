from treenode import TreeNode
from binarysearchtree import BinarySearchTree

class TestHelper:
    @staticmethod
    def test_0():
        root0=TreeNode(10,TreeNode(5,None,None),TreeNode(15,None,None))
        return(BinarySearchTree.isBinarySearchTree(root0)==True)

    @staticmethod
    def test_1():
        root1=TreeNode(20,TreeNode(5,None,None),TreeNode(15,None,None))
        return(BinarySearchTree.isBinarySearchTree(root1)==False)

    @staticmethod
    def test_2():
        root2=TreeNode(20,TreeNode(10,None,TreeNode(25,None,None)),TreeNode(30,None,None))
        return(BinarySearchTree.isBinarySearchTree(root2)==False)

    @staticmethod
    def test_3():
        root3=TreeNode(10,TreeNode(10,None,None),None)
        return(BinarySearchTree.isBinarySearchTree(root3)==True)

    @staticmethod
    def test_4():
        root4=TreeNode(10,None,TreeNode(10,None,None))
        return(BinarySearchTree.isBinarySearchTree(root4)==False)

    @staticmethod
    def test_5():
        root5=None
        return(BinarySearchTree.isBinarySearchTree(root5)==True)

    @staticmethod
    def test_6():
        root6=TreeNode(8,TreeNode(2,None,None),TreeNode(6,TreeNode(4,None,None),None))
        return(BinarySearchTree.isBinarySearchTree(root6)==False)

    @staticmethod
    def test_7():
        root7=TreeNode(0,TreeNode(0,TreeNode(0,None,None),None),None)
        return(BinarySearchTree.isBinarySearchTree(root7)==True)

    @staticmethod
    def test_8():
        root8=TreeNode(0,None,TreeNode(0,None,TreeNode(0,None,None)))
        return(BinarySearchTree.isBinarySearchTree(root8)==False)

    @staticmethod
    def test_9():
        root9=TreeNode(20,TreeNode(10,TreeNode(5,TreeNode(3,None,None),TreeNode(7,None,None)),TreeNode(15,None,TreeNode(17,None,None))),TreeNode(30,None,None))
        return(BinarySearchTree.isBinarySearchTree(root9))

if __name__ == "__main__":
    print(TestHelper.test_0())
    print(TestHelper.test_1())
    print(TestHelper.test_2())
    print(TestHelper.test_3())
    print(TestHelper.test_4())
    print(TestHelper.test_5())
    print(TestHelper.test_6())
    print(TestHelper.test_7())
    print(TestHelper.test_8())
    print(TestHelper.test_9())
