#https://programmers.co.kr/learn/courses/30/lessons/42586
def solution(progresses, speeds):
    from collections import deque

    answer = []
    prog =deque(progresses)
    speed = deque(speeds)
    count = 0

    # prog = [x + y for x,y in zip(prog,speed)]


    while prog:#[98 100 55]

        for index in range(len(prog)):
            prog[index] += speed[index]
        for index in range(len(prog)):
            if prog[0]>=100 and prog[index]>=100:
                count+=1
            else:
                break

        for index in range(len(prog)):
            if prog[0]>=100:
                prog.popleft()
                speed.popleft()
                answer.append(count)
                count=0
                if 0 in answer:
                    answer.remove(0)

    return answer



print(solution([93,30,55],[1,30,5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
