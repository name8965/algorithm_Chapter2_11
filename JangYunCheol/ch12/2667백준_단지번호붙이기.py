import copy
def soultion(list):

    map = copy.deepcopy(list)
    number ={}
    for i in range(len(list)):
        number[i]=0
    num =1
    count =0
    x = len(list)
    y = len(list[0])
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    def dfs(i:int,j:int):   #재귀 방문 처리
        if i<0 or i>=x or j<0 or j>=y or list[i][j] != 1:
            return

        map[i][j] = num
        number[num]=number[num]+1
        list[i][j] = 0
        for k in range(4):
            dfs((i+dx[k]),(j+dy[k]))
        return

    #검색 및 다른 단지 처리
    for i in range(x):
        for j in range(y):
            node = list[i][j]
            if node ==0:
                continue
            count +=1
            num +=1
            dfs(i,j)

    #출력
    print(count)
    list_prt= []
    for i in number:
        if number[i]!=0:
            list_prt.append(number[i])
    list_prt.sort()
    for i in range(len(list_prt)):
        print(list_prt[i])
    return








# map = [[0,1,1,0,1,0,0],
#         [0,1,1,0,1,0,1],
#         [1,1,1,0,1,0,1],
#         [0,0,0,0,1,1,1],
#         [0,1,0,0,0,0,0],
#         [0,1,1,1,1,1,0],
#         [0,1,1,1,0,0,0]]
# soultion(map)


n = int(input())
map2 = []
for i in range(n):
    map2.append(list(map(int, input())))
soultion(map2)


