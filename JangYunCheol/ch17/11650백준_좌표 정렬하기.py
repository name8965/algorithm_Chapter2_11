
import sys
def quicksort(lst,start,end):
    def partition(plst,ps,pe):
        pivet = plst[pe][0]
        i = ps -1
        for j in range(ps,pe):
            if lst[j][0]<=pivet:
                i+=1
                lst[i][0],lst[j][0] = lst[j][0],lst[i][0]
        lst[i+1][0],lst[pe][0] = lst[pe][0],lst[i+1][0]
        return i+1



    if start>=end:
        return None

    p = partition(lst,start,end)
    quicksort(lst,start,p-1)
    quicksort(lst,p+1,end)

    return lst

import sys
input = sys.stdin.readline

tc = int(input())
lst = []
for _ in range(tc):
    n,m = map(int, input().split())

    lst.append((m,n))
lst.sort()
# quicksort(lst,0,len(lst))
for y,x in lst:
    print(x,y)
# import sys
# input = sys.stdin.readline
#
# tc = int(input())
# lst = []
# for _ in range(tc):
#     n,m = map(int, input().split())
#
#     lst.append((m,n))
# lst2 =sorted(lst)
# # quicksort(lst,0,len(lst))
# for y,x in lst2:
#     print(x,y)


# print(lst)



"""
5
3 4
1 1
1 -1
2 2
3 3

5
0 4
1 2
1 -1
2 2
3 3
"""