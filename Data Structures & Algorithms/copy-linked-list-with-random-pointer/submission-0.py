"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        mp = dict({None: None})
        while curr:
            node = Node(curr.val)
            mp[curr] = node
            curr = curr.next

        curr = head
        while curr:
            temp = mp[curr]
            temp.random = mp[curr.random]
            temp.next = mp[curr.next]
            curr = curr.next
        return mp[head]
