# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag_(self, root: Optional[TreeNode]) -> (int, int, int):
        if root is None:
            return (0, 0, 0)
        left = 1
        right = 1
        mx = 1
        if root.left is not None:
            ll, lr, lmx = self.longestZigZag_(root.left)
            left += lr
            mx = max(mx, ll, left, lmx)
        if root.right is not None:
            rl, rr, rmx = self.longestZigZag_(root.right)
            right += rl
            mx = max(mx, rr, right, rmx)
        return left, right, mx
            
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        return self.longestZigZag_(root)[-1] - 1
