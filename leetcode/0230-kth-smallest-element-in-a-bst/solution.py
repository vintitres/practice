# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def size(node: Optional[TreeNode]) -> int:
        if node == None:
            return 0
        return 1 + Solution.size(node.left) + Solution.size(node.right)

        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        size_left = Solution.size(root.left)
        if size_left >= k:
            return self.kthSmallest(root.left, k)
        if size_left == k - 1:
            return root.val
        return self.kthSmallest(root.right, k - size_left - 1)
        """
        cnt = 0
        queue = deque([(root, False)])
        while queue:
            node, processed = queue.popleft()
            print(node.val, processed)
            if not processed:
                if node.right:
                    queue.appendleft((node.right, False))
                queue.appendleft((node, True))
                if node.left:
                    queue.appendleft((node.left, False))
            else:
                cnt += 1
                if cnt == k:
                    return node.val




        
