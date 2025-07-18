# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        traversal = [[]]
        queue = deque([(root, 0)])
        traversal_level = 0
        while queue:
            _, level = queue[0]
            if level != traversal_level:
                traversal.append([])
                traversal_level = level
            node, level = queue.popleft()
            traversal[-1].append(node.val)

            if node.left is not None:
                queue.append((node.left, level + 1))
            if node.right is not None:
                queue.append((node.right, level + 1))
        return traversal


        

        
