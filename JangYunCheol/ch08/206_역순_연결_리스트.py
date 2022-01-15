# Definition for singly-linked list.
#219
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None #연결리스트의 이전 위치 초기는 마지막위치 이므로 None
        cur = head  #사용할 변수 링크 선언 (일종의 temp)헤드값을 담아 놓음#초기 값 연결리스트 = 연결리스트는 헤드를 알면 전체를 알수있다
        while cur:  #헤드(연결리스트)의 길이 만큼 while를 반복
            next = cur.next  #다음 가야할 곳을 담아 놓음 일종의 Temp2
            cur.next = prev  #헤드의 next에 이전리스트를 연결 반전시킴/N 1->2->3->N 이였던걸 N<-1 2->3->N 으로 바꿈
            prev = cur       #이전리스트에 curr 일종에 cur 은 위치를 알려주는 역활
            cur = next       #다음 가야할 곳에 cur 일종의 위치를 알려주는 아이를 보냄
        return prev

s = Solution()
listn = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
print(s.reverseList(ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))))
print(listn)
print(listn)