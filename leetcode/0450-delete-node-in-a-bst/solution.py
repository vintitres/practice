# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is not None:
                last_node = root
                last_dir = "L"
                node = root.left
                while node.right is not None:
                    last_node = node
                    last_dir = "R"
                    node = node.right
                root.val = node.val
                if last_dir == "R":
                    last_node.right = node.left
                else:
                    last_node.left = node.left
            elif root.right is not None:
                last_node = root
                last_dir = "R"
                node = root.right
                while node.left is not None:
                    last_dir = ""
                    last_node = node
                    node = node.left
                root.val = node.val
                if last_dir == "R":
                    last_node.right = node.right
                else:
                    last_node.left = node.right
            else:
                return None
        return root

        
