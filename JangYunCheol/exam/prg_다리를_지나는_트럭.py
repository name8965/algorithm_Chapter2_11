#https://programmers.co.kr/learn/courses/30/lessons/42583#
def solution(bridge_length, weight, truck_weights):
    from collections import deque

    # answer = 0
    # truck_weights = deque(truck_weights)
    # b_weight = deque()
    # count = 0
    # temp = truck_weights.copy()
    # size = len(truck_weights)
    # result_list , b_len = deque(),deque()
    #
    #
    #
    #
    # while len(result_list)<size:
    #     answer += 1
    #
    #
    #
    #     if truck_weights :
    #         if(sum(b_weight,truck_weights[0])<=weight) \
    #                 and len(b_weight) +1<=bridge_length:
    #             b_weight.append(truck_weights[0])
    #             b_len.append(0)
    #             truck_weights.popleft()
    #
    #     for i in range(len(b_len)):
    #         b_len[i] += 1
    #
    #     if b_len:
    #         if b_len[0] > bridge_length:
    #             b_len.popleft()
    #             result_list.append(b_weight.popleft())
    #             if truck_weights:
    #                 if (sum(b_weight, truck_weights[0]) <= weight) \
    #                         and len(b_weight) + 1 <= bridge_length:
    #                     b_weight.append(truck_weights[0])
    #                     b_len.append(0)
    #                     truck_weights.popleft()
    #
    #             for i in range(len(b_len)):
    #                 b_len[i] += 1
    #
    # return answer

    answer = 0
    truck_weights = deque(truck_weights)
    b_weight = deque()
    temp = truck_weights.copy()
    size = len(truck_weights)
    result_list = deque()
    b_len = deque([0]*bridge_length)

    while len(result_list) < size:
        answer += 1
        top = b_len.popleft()
        if top!=0:
            result_list.append(top)
            b_weight.popleft()

        if truck_weights:
            if (sum(b_weight)+ truck_weights[0]) <= weight and len(b_weight) + 1 <= bridge_length:
                b_weight.append(temp.popleft())
                b_len.append(truck_weights.popleft())
            else:
                b_len.append(0)

    return answer


# 3,10,[2,3,6,7]








    return answer

print(solution(2,10,[7,4,5,6]))



# test1 = [1,2,3,4,5]
# test2 = test1         #얕은 복사
#
# print(test1,test2)
#
# test2.pop()
# print(test1,test2)
#
# test1 = [1,2,3,4,5]
# test2 = test1.copy() #깊은 복사  copy/deepcopy 차이는 이중배열같은걸 완전히 처리해주지않음
#                     #tuple사용하기
#
#
# print(test1,test2)
#
# test2.pop()
# print(test1,test2)
