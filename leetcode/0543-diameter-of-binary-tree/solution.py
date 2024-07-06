# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(node):
            if node is None:
                return (-1,0)
            lh, ld = helper(node.left)
            rh, rd = helper(node.right)
            d_through_self = lh + rh + 2
            h = max(lh, rh) + 1
            d = max(ld, rd, d_through_self)
            return (h, d)

        return helper(root)[1]
        
