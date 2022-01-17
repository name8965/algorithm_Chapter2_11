from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head and head.next:
            p = head.next
            head.next = self.swapPairs(p.next)
            p.next = head

            return p
        return head






        #값 교환 방식
        # cur = head
        # while cur and cur.next:
        #     cur.val,cur.next.val = cur.next.val,cur.val
        #     cur= cur.next.next
        #
        # return head


s = Solution()
listn = ListNode(1,ListNode(2,ListNode(3,ListNode(4))))
print(s.swapPairs(listn))
print(listn)
print(listn)