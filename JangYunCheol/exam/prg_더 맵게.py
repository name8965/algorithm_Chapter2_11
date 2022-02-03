#https://programmers.co.kr/learn/courses/30/lessons/42626

"""
리스트 솔트 => 리스트에서 0번째 값이 k보다 큰지확인 후
작다면 0번째 1번째를 popleft해서 0번째+(1번째*2)후 다시 리스트에 appendleft
카운트++
"""
import heapq


def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)

    while len(scoville)>=2:
        h_min = heapq.heappop(scoville)
        if h_min>=K:
            return answer

        else:
            h_min2 = heapq.heappop(scoville)
            heapq.heappush(scoville,h_min+h_min2*2)
            answer+=1
    if scoville[0]>K:
        return answer
    else:
        return -1
    # if not scoville or len(scoville)<2:
    #     return -1
    # def run(lst,k):
    #     count =0
    #     heapq.heapify(lst)
    #
    #     if lst[0]>k or len(lst)<2:
    #         return 0
    #     arr1 = heapq.heappop(lst)
    #     arr2 = heapq.heappop(lst)
    #     asum=arr1+(arr2*2)
    #     heapq.heappush(lst,asum)
    #     count+=1
    #     count +=run(lst,k)
    #     return count
    #
    # answer+=run(scoville,K)
    # return answer


print(solution([1],11))
print(solution([1, 2, 3]	,11))
print(solution([1, 2, 3, 9, 10, 12]	,7))