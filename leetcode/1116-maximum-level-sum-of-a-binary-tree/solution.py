# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append((root, 1))
        cur_sum = 0
        cur_level = 1
        max_sum = None
        max_sum_level = None
        while len(q) > 0:
            (node, level) = q.popleft()
            if node is None:
                continue
            if level == cur_level:
                cur_sum += node.val
            else:
                if max_sum is None or cur_sum > max_sum:
                    max_sum = cur_sum
                    max_sum_level = cur_level
                cur_sum = node.val
                cur_level = level
            q.append((node.left, level + 1))
            q.append((node.right, level + 1))
        if max_sum is None or cur_sum > max_sum:
            return cur_level
        return max_sum_level
        
