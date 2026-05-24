# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        
        # Now for each k groups reverse the nodes
        prev = dummy
        curr = None
        temp = None
        while n >= k:
            curr = prev.next
            temp = curr.next
            for _ in range(1, k):
                curr.next = temp.next
                temp.next = prev.next
                prev.next = temp
                temp = curr.next
            prev = curr
            n -= k
        return dummy.next