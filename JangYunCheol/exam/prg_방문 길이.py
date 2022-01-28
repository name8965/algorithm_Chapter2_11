#https://programmers.co.kr/learn/courses/30/lessons/49994
def solution(dirs):
    # from collections import deque
    # cy = 5
    # cx = 5
    # answer = set()
    # visite=0
    # q = deque(dirs)
    # while q :
    #     move = q.popleft()
    #     if move =='U' and cy<11:
    #         answer.add(((cx,cy),(cx,cy+1)))
    #         answer.add(((cx,cy+1),(cx,cy)))
    #         cy+=1
    #         visite+=1
    #     elif move == "D" and cy>0:
    #         answer.add(((cx, cy-1), (cx, cy)))
    #         answer.add(((cx, cy), (cx, cy-1)))
    #         cy-=1
    #         visite+=1
    #
    #     elif move == "L" and cx>0:
    #         answer.add(((cx,cy),(cx-1,cy)))
    #         answer.add(((cx-1,cy),(cx,cy)))
    #         cx-=1
    #         visite+=1
    #
    #     elif move == "R" and cx<11:
    #         answer.add(((cx,cy),(cx+1,cy)))
    #         answer.add(((cx+1,cy),(cx,cy)))
    #         cx+=1
    #         visite+=1
    #
    #
    # return visite
    from collections import deque
    cx ,cy= 5,5
    dx,dy = [-1,0,1,0],[0,-1,0,1]
    answer = 0
    map_d = {"U": 0, "L":1, "D":2, "R": 3}
    visite = set()
    q = deque(dirs)
    while q:
        move = q.popleft()
        d = map_d[move]
        nx,ny = cx+dx[d],cy+dy[d]
        if nx>11 or nx<0 or ny>11 or ny<0:
            continue
        if (cx,cy,nx,ny) not in visite:
            visite.add((cx,cy,nx,ny))
            visite.add((nx,ny,cx,cy))
            answer+=1
        cx,cy = nx,ny

    return answer



print(solution("LRLRL"))
print(solution("LULLLLLLU"))