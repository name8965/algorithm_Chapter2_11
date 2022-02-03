
import sys
tc = int(sys.stdin.readline())
lst = []
for i in range(tc):
    lst.append(int(sys.stdin.readline()))

lst.sort()
for i in lst:
    print(i)