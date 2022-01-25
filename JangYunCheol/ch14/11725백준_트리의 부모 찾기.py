


import sys
sys.setrecursionlimit(10 ** 9)
import collections
def findparent(n):
    for i in tree[n]:
        # print(i)
        if result[i]==0:
            result[i]=n
            findparent(i)



number = int(input())
# tree = [[] for _ in range(number+1)]
tree = collections.defaultdict(list)
result = [0]*(number+1)
for i in range(number-1):
    n,m = map(int, input().split())
    tree[n].append(m)
    tree[m].append(n)


# print(tree)

findparent(1)

# print(result)

# print("result")
for i in range(2,number+1):
    print(result[i])