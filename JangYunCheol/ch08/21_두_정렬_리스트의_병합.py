#p213
from typing import List
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy =cur=ListNode(0) #반복문 방식
        #
        # while list1 and list2:
        #     if list1.val<list2.val:
        #         cur.next = list1
        #         list1 = list1.next
        #     else:
        #         cur.next = list2
        #         list2 = list2.next
        #     cur=cur.next
        # cur.next = list1 or list2
        # return dummy.next


        # 재귀방식 [124][134]
        if list1 is None or list2 is None:  #base case 재귀 탈출용
            return list1 or list2
        if list1.val < list2.val: #1번 리스트가 더 작을때 1번 리스트에 다음번째에 재귀를 호출
            list1.next = self.mergeTwoLists(list1.next,list2) #236
            return list1
        else:
            list2.next = self.mergeTwoLists(list1,list2.next) #145
            return list2 #2번 리스트가 더 작을땐 2번 리스트의 다음 번째를 넘겨주며 재귀를 호출





s = Solution()
list1=ListNode(1,ListNode(2,ListNode(4)))
list2=ListNode(1,ListNode(3,ListNode(4)))
print(s.mergeTwoLists(ListNode(1,ListNode(2,ListNode(4))),ListNode(1,ListNode(3,ListNode(4)))))

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

print(l1)
print(list2)
print("------------")

