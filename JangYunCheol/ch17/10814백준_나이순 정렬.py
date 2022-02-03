from typing import List






import sys
tc = int(sys.stdin.readline())
lst = []
for i in range(tc):
    n, m = map(str, input().split())
    lst.append([int(n),m])



lst = sorted(lst,key=lambda x:x[0])

for i in lst:
    print(i[0], i[1])