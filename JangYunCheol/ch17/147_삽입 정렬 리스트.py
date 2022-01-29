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
#[4,2,1,3]
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node =ListNode(None,head)
        key = head
        cur = head.next
        while cur:
            if cur.val >=key.val:                       #정렬이 되어있으면 키를 넘기고 while문 마지막 줄로 인해 cur은 키의 다음값으로 이동함
                key = key.next
            else:
                prev = dummy_node
                while prev.next is not None and prev.next.val <= cur.val:   #비교할 대상하고 이전 노드가 바뀔만하지 물어봄
                    prev= prev.next

                key.next = cur.next
                cur.next = prev.next
                prev.next = cur
            cur = key.next

        return dummy_node.next

    #     lst = self.NodeTolist(head)
    #
    #     for i in range(1,len(lst)):
    #         for j in range(1,i+1):
    #             cur = i-j
    #             if lst[cur] >lst[cur+1]:
    #                 lst[cur],lst[cur+1] = lst[cur+1],lst[cur]
    #             else:
    #                 break
    #     return self.listToNode(lst)
    #
    # def NodeTolist(self,head):
    #     lst = []
    #     while head:
    #         lst.append(head.val)
    #         head = head.next
    #     return lst
    #
    # def listToNode(self,lst):
    #     head = None
    #     while lst:
    #         head = ListNode(lst.pop(), head)
    #     return head







s = Solution()



tc1 = listToNode([4,2,1,3])
tc2 = listToNode([-1,5,3,4,0])


print(s.insertionSortList(tc1))
print(s.insertionSortList(tc2))
