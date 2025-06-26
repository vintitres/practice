# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tens = 1
        sum = 0
        while l1 is not None or l2 is not None:
            if l1 is not None:
                sum += tens * l1.val
                l1 = l1.next
            if l2 is not None:
                sum += tens * l2.val
                l2 = l2.next
            tens *= 10
        sumlist = ListNode(sum % 10)
        end = sumlist
        sum //= 10
        while sum > 0:
            end.next = ListNode(sum % 10)
            sum //= 10
            end = end.next
        return sumlist
