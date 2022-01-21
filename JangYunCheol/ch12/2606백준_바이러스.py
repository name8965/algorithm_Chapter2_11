def virus(node,visite):
    visite.append(node) #들어간 노드를 리스트에 넣어줌
    for adj in map[node]: #딕셔너리에 노드 키 중
        if adj not in visite:   #이미 리스트에 들어있는지 확인
            virus(adj,visite)   #없으면 재귀 호출
    return len(visite)-1    #자기자신을 제외한 감염된 컴퓨터 수


map = {1: [2, 5],
       2: [1, 3, 5],
       3: [2],
       4: [7],
       5: [1, 2, 6],
       6: [5],
       7: [4]
       }

# n = int(input())
# m = int(input())
#
# map = {}
# for i in range(1,n+1):
#     map[i] = set()
#
# for _ in range(m):
#     a, b = input().split()
#     map[int(a)].add(int(b))
#     map[int(b)].add(int(a))





print(virus(1,[]))
