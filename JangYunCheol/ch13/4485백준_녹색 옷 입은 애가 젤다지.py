import sys
import heapq

def dijkstar():
    heap = []
    heapq.heappush(heap,(graph[0][0],0,0))
    dist[0][0]=0

    while heap:
        cost,x,y = heapq.heappop(heap)

        if x==n-1 and y==n-1:
            print('Problem',end=" ")
            print(count,end="")
            print(':',end=" ")
            print(dist[x][y])

        for i in range(4):
            nx= x+dx[i]
            ny= y+dy[i]

            if nx<n and ny<n and 0<=nx and 0<=ny:
                ncost = cost+graph[nx][ny]

                if ncost <dist[nx][ny]:
                    dist[nx][ny]=ncost
                    heapq.heappush(heap,(ncost,nx,ny))


input = sys.stdin.readline
INF = sys.maxsize

dx=[-1,1,0,0]
dy=[0,0,-1,1]

count =1
while True:
    n = int(input())
    if n==0:
        break
    graph = [list(map(int,input().split())) for _ in range(n)]
    dist = [[INF] * n for _ in range(n)]

    dijkstar()
    count+=1