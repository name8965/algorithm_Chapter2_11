from typing import List
from itertools import combinations
def pawd(paslist:List[str],num:int):

    result = []
    # comb = list(mycomb(paslist,num))
    comb = combinations(paslist,num)
    sortlist = []

    for i in comb:
        sortlist.append(sorted(i))

    for i in sorted(sortlist):
        vowel = 0 #모음
        consonant = 0 #자음
        for j in i:
            if j in 'aeiou':
                vowel+=1
            else:
                consonant+=1
        if vowel>=1 and consonant>=2:
            print("".join(i))




L, C = map(int, input().split())

li = list(map(str, input().split()))
pawd(li,L)
# print(pawd(['a', 'b', 'c', 'd', 'e', 'f'],4))
# print(pawd(['a', 't', 'c', 'i', 's', 'w'],4))
# print(mycomb(['a', 't', 'c', 'i', 's', 'w'],4))
def mycomb(list,num):
    result = []

    if num>len(list):
        return result
    if num==1:
        for i in list:
            result.append([i])

    elif num>1:
        for i in range(len(list)-num+1):
            for j in mycomb(list[i+1:],num-1):
                result.append([list[i]]+j)
    return result