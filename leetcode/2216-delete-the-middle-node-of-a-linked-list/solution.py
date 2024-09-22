# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def length(self, head: Optional[ListNode]) -> int:
        if head is None:
            return 0
        return 1 + self.length(head.next)

    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = self.length(head)
        if length <= 1:
            return None
        index_to_delete = int(length / 2)
        last_node = head
        node = head.next
        for i in range(index_to_delete - 1):
            last_node = node
            node = node.next
        last_node.next = node.next 
        return head


        
