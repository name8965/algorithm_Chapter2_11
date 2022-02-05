import sys


def solution(lst):
    for i in range(len(lst)):


        if i<len(lst) and lst[i] == i:
            return i

    return -1


tc = int(sys.stdin.readline())
n = list(map(int,sys.stdin.readline().split()))
print(solution(n))




"""
5
-15 -6 1 3 7
"""