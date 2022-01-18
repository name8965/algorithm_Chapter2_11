from collections import deque


def print_que(n,m,imp):
    if len(imp)<m+1:            #예외처리 리스트보다 찾는 번호수가 클때
        return -1
    idx = deque(range(len(imp))) #인덱스를 담는 데큐
    imp = deque(imp)             #중요도를 담는 데큐
    target =idx[m]              #타겟 인덱스 번호의 중요도값
    count = 0                   #몇번째인지

    while True:
        if imp[0]==max(imp):        #데큐의 0번째 값이 데큐에서 가장 큰 값과 같으면  [123]
            count+=1                                                         #[012]

            if idx[0] ==target:
                return count
            else:
                imp.popleft()
                idx.popleft()
        else:
            imp.append(imp.popleft())
            idx.append(idx.popleft())

#
# test_case = int(input())
#
# for _ in range(test_case):
#     n,m = list(map(int, input().split()))
#     imp = list(map(int, input().split()))
#     idx = deque(range(len(imp)))
#     print(print_que(n,m,imp))
#     idx[m]='target'
#
# print(test_case)



print(print_que(4,2,[1,2,3,4]))
print(print_que(6,0,[1,1,9,1,1,1]))
print(print_que(6,0,[1,1,9,1,1,1]))

# import sys
#
#
# T = int(sys.stdin.readline())   # 입력받을 숫자
#
# for i in range(T):
#     VPS = sys.stdin.readline()
# print(map[1,2])