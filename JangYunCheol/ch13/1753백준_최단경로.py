import sys
import heapq

def dijkstar(start):
    dp[start] = 0
    heapq.heappush(heap,(0,start))

    while heap:
        acc,now = heapq.heappop(heap)

        if dp[now]<acc:
            continue

        for cur,next_node in graph[now]:
            cost = acc + cur
            if cost<dp[next_node]:
                dp[next_node] =cost
                heapq.heappush(heap,(cost,next_node))

input = sys.stdin.readline
INF = sys.maxsize
V, E = map(int, input().split())

K = int(input())
#시작점

dp = [INF] * (V+1)

heap=[]
graph = [[]for _ in range(V+1)]

for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u].append((w,v))

dijkstar(K)


for i in range(1,V+1):
    if dp[i]==INF:
        print("INF")
    else:
        print(dp[i])
