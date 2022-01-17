#p233
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:    #그냥하니 Tc로 []값 보내줌...
            return head
        odd = head #초기 홀수번째 키값=헤드값
        even = head.next    #짝수번째라는 값을 위해 초기 값의 다음값
        even_head = head.next   #짝수번째의 키값을 위해 미리 헤드를 변수에 저장해둠
        while even and even.next:   #다음값이 None까지(끝까지) 반복
            odd.next = odd.next.next    #홀수번째의 다음번째를 다다음으로 바꿔서 땡겨옴
            even.next = even.next.next  #짝수번째의 다음번째를 다다음으로 바꿔서 땡겨옴
            odd = odd.next              #땡겨져 온 2번째 홀수번째를 다음 연산을 위해 교체
            even = even.next            #땡겨져 온 2번째 짝수번째를 다음 연산을 위해 교체
        odd.next = even_head            #마지막 홀수번째(마지막홀수번째의 다음은 None상태)의
                                        # 짝수번째의 처음 값을 넣음

        return head

s = Solution()
listn = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

print(s.oddEvenList(listn))
print(s.oddEvenList(listn))