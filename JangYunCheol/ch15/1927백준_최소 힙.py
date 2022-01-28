# 9
# 0
# 12345678
# 1
# 2
# 0
# 0
# 0
# 0
# 32
#9번 입력/x 가 0이면 가장 작은값 출력/ 힙이 비어있으면 0출력/ x가 0이 아니면 힙에 푸시


"""heapq 모듈

# heapq.heappush(heap, item) : item을 heap에 추가 : 최소힙
# for num in nums:
#   heapq.heappush(heap, (-num, num)) : 최대 힙 (우선순위,값)

# heapq.heappop(heap) : heap에서 가장 작은 원소를 pop & 리턴. 비어 있는 경우 IndexError가 호출됨.
# heapq.heapify(x) : 리스트 x를 즉각적으로 heap으로 변환함 (in linear time, O(N) )
"""
import sys
import heapq
def minheap(x,heap):

    if x == 0:
        if heap:
            # 가장 작은값출력
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap,x)

    return heap

heap = []
n = int(sys.stdin.readline())
for _ in range(n):
    x = int(sys.stdin.readline())
    heap = minheap(x,heap)



#시간초과
# import sys
# def minheap(x,heap):
#
#     if x == 0:
#         if heap:
#             # 가장 작은값출력
#             print(heap.pop())
#         else:
#             print(0)
#     else:
#         heap.append(x)
#         heap = sorted(heap,reverse=True) #내림차순정렬
#
#     return heap
#
# heap = []
# n = int(sys.stdin.readline())
# for _ in range(n):
#     x = int(sys.stdin.readline())
#     heap = minheap(x,heap)