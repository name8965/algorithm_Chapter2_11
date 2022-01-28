"""
test = [4, 1, 7, 3, 8, 5]
for num in test:
    heapq.heappush(heap, (-num, num))
while heap:
    print(heapq.heappop(heap)[1])
    (-8,8) 형태로 들어가다보니 최소값순으로 정렬되지만(-8이 가장작으므로)
    출력할땐 괄호에서 1번째를 뽑다보니 큰값부터 출력됨

"""



import sys
import heapq
def maxheap(x,heap):

    if x == 0:
        if heap:
            # 가장 작은값의 1번째 출력
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap,(-x,x))

    return heap

heap = []


n = int(sys.stdin.readline())
for _ in range(n):
    x = int(sys.stdin.readline())
    heap = maxheap(x,heap)

