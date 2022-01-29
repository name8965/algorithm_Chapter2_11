# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


def listToNode(lst):
    head = None
    while lst:
        head = ListNode(lst.pop(),head)
    return head

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # node = ListNode(0)
        # while head:
        #     key = node
        #     while key:
        #         if head.val >= key.val and (key.next == None or (head.val<=key.next.val)):
        #             next =  head.next
        #             head.next = key.next
        #             key.next = head
        #             head = next
        #             break
        #         if head and key.val >key.next.val:
        #           key = key.next
        # return node.next

        lst = self.NodeTolist(head)

        for i in range(1,len(lst)):
            for j in range(1,i+1):
                cur = i-j
                if lst[cur] >lst[cur+1]:
                    lst[cur],lst[cur+1] = lst[cur+1],lst[cur]
                else:
                    break
        return self.listToNode(lst)

    def NodeTolist(self,head):
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        return lst

    def listToNode(self,lst):
        head = None
        while lst:
            head = ListNode(lst.pop(), head)
        return head







s = Solution()



tc1 = listToNode([4,2,1,3])
tc2 = listToNode([-1,5,3,4,0])

print(s.insertionSortList(tc1))
print(s.insertionSortList(tc2))
