# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head: return

        dummy = ListNode(-1)
        dummy.next = head
        curr = dummy
        
        totalLen = 0
        while curr:
            curr = curr.next
            totalLen += 1
        
        n = n % totalLen
        curr = dummy
        for _ in range(totalLen - n - 1):
            curr = curr.next
        
        curr.next = curr.next.next
        return dummy.next