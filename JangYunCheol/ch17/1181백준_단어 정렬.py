from typing import List


def merge(arr1, arr2):
    result = []
    resultlen = []
    arrlen1 = []
    arrlen2 = []

    for i in arr1:
        arrlen1.append(len(i))
    for i in arr2:
        arrlen2.append(len(i))

    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arrlen1[i] < arrlen2[j] :
            result.append(arr1[i])
            resultlen.append(arrlen1[i])
            i += 1
            continue

        if arrlen1[i] == arrlen2[j]:
            if arr1[i] < arr2[j]:
                result.append(arr1[i])
                resultlen.append(arrlen1[i])
                i += 1
                continue

        result.append(arr2[j])
        resultlen.append(arrlen2[j])
        j += 1

    while i < len(arr1):
        result.append(arr1[i])
        resultlen.append(arrlen1[i])
        i += 1

    while j < len(arr2):
        result.append(arr2[j])
        resultlen.append(arrlen2[j])
        j += 1
    temp = []
    temp.append(result[0])
    for a in range(len(result)):
        if temp[-1] !=result[a]:

           temp.append(result[a])

    return temp
def mysort(lst:List[str],lstlen:List[int]):
    if len(lst) <=1:
        return lst



    mid = len(lst)//2
    L = lst[:mid]
    Ll = lstlen[:mid]
    R = lst[mid:]
    Rl = lstlen[mid:]
    return merge(mysort(L,Ll),mysort(R,Rl))










lst = []
lstlen = []

# lst = [['but'], ['i'], ['wont'], ['hesitate'], ['no'], ['more'], ['no'], ['more'], ['it'], ['cannot'], ['wait'], ['im'], ['yours']]
# for i in lst:
#     lstlen.append(len(i[0]))
# result = mysort(lst,lstlen)
# for i in result:
#     print(''.join(i))
#
# ['but', 'i', 'wont', 'hesitate', 'no', 'more', 'no', 'more', 'it', 'cannot', 'wait', 'im', 'yours']

# import sys
# tc =int(sys.stdin.readline())
#
# for _ in range(tc):
#     n = sys.stdin.readline().rstrip()
#     lst.append(n)
#
# result = mysort(lst,lstlen)
# for i in result:
#     print(''.join(i))

"""    
13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours
"""

import sys
tc =int(sys.stdin.readline())

for _ in range(tc):
    n = sys.stdin.readline().rstrip()
    lst.append(n)
slst = list(set(lst))
slst.sort()
slst.sort(key=len)
for i in slst:
    print(i)