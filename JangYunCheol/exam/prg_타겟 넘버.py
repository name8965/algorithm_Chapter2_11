#https://programmers.co.kr/learn/courses/30/lessons/43165
from typing import List

import sys
sys.setrecursionlimit(10 ** 9)

def solution(numbers, target):


    answer = 0
    answer += dfs(numbers, target, 0)
    return answer
def dfs(number, tar, lens):
    result = 0
    if lens == len(number):
        if sum(number) == tar:
            return 1
        else:
            return 0
    else:
        result += dfs(number,tar,lens+1)
        number[lens] *=-1
        result += dfs(number,tar,lens+1)

    return result






def solution2(numbers, target):
    if not numbers and target == 0:
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target - numbers[0]) + solution(numbers[1:], target + numbers[0])



    # if not number:
    #     return
    # if tar == result and lens ==0:
    #     answer+=1
    #     return
    # if lens<0:
    #     return
    # num = number[4]
    # forrange = [num,-num]
    # for i in forrange:
    #     dfs(number, tar, len(number))
    # number.pop()
print(solution([1,1,1,1,1],3))