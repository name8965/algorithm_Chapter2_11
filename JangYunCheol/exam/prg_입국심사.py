# https://programmers.co.kr/learn/courses/30/lessons/43238

def solution(n, times):
    answer = 0
    start,end = 1,max(times)*n
    while start <= end:
        mid = (start + end) // 2
        people = 0

        for i in times:
            people += mid//i
        if people >= n:
            answer = mid
            end = mid - 1
        if people < n:
            start = mid + 1

    return answer



print(solution(6,[10, 7]))