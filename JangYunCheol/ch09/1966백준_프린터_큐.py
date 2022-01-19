from collections import deque
#선입선출(FIFO)인 프린터에서 중요도란 수치가 추가되었다.
#현재 Queue의 가장 앞(0번째)에 있는 문서의 '중요도'를 확인한다
#나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 있다면
#이 문서를 Queue의 가장 뒤로 재배치 한다. 그렇지 않다면 바로 인쇄한다


#Queue의 0번째가 중요도가 가장 높은지 확인하고 출력할지 Queue의 맨뒤로갈지 결정한다

#현재 Queue에 있는 문서의 수와 중요도가 주어졌을때  = input : 문서의수/ 중요도
#어떠 한개의 문서가 몇 번째로 인쇄되는지 출력한다
#ex> (A B  D)가 있으면 A가 몇번째로 출력되는지?? =(Target)
#중요 (2 1  3)   출력순서는 C->D->A->B 순서이므로 3번재


#[1,2,3,4]
#[0,1,2,3]
def print_que(n,m,imp):
    if len(imp)<m+1:            #예외처리 리스트보다 찾는 번호수가 클때
        return -1

    idx = deque(range(len(imp))) #인덱스를 담는 데큐
    imp = deque(imp)             #중요도를 담는 데큐
    target =idx[m]              #타겟 인덱스 번호의 중요도값
    count = 0                   #몇번째인지

    while True:
        if imp[0]==max(imp):        #데큐의 0번째 값이 데큐에서 가장 큰 값과 같으면  [1234]
            count+=1                                                         #[0123]

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
