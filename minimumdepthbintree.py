# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):


    def getMinDepth(self, root):
        if root == None: return float("inf")
        if root.left == None and root.right == None: return 1
        else:
            return 1 + min(self.getMinDepth(root.left),
                        self.getMinDepth(root.right))


    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0
        else: return self.getMinDepth(root)
