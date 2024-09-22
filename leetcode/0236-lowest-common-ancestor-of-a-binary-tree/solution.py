# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def find_path(self, root: Optional['TreeNode'], node: 'TreeNode') -> Optional[List['TreeNode']]:
        if root is None:
            return None
        if root == node:
            return [root]
        path_left = self.find_path(root.left, node)
        if path_left is not None:
            return [root] + path_left
        path_right = self.find_path(root.right, node)
        if path_right is not None:
            return [root] + path_right
        return None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path_p = self.find_path(root, p)
        path_q = self.find_path(root, q)

        #print(path_p)
        #print(path_q)

        last_node = None
        for path_p_node, path_q_node in zip(path_p, path_q):
            if path_p_node != path_q_node:
                break
            last_node = path_p_node
        return last_node

    
