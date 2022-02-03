#https://programmers.co.kr/learn/courses/30/lessons/17686
"""
문자의 사전순/숫자순/입력된순
"""
# import re


# def solution(files):
#     answer = []
#     for i in range(len(files)):
#         text = files[i]
#         num = re.findall(r'\d+',text)[0]  #리스트로 반환되길래
#         for j in range(len(text)):
#             if text[j:len(num)+j]==num:
#                 head = text[:j]
#                 tail = text[len(num)+j:]
#                 answer.append((head,num,tail,i))
#     answer = sorted(answer,key=lambda x:(x[0].lower(),int(x[1]),x[3]))
#     result =[]
#     for i in answer:
#         print(''.join(i[:3]))  #튜플형태라
#         result.append(''.join(i[:3]))
#     return result
def splits_files(files):
    files_list = []
    for index,file in enumerate(files):
        file = file.lower()
        num_list = []
        flag = False
        for s,f in enumerate(file):
            if f in "0123456789":
                flag = True
                num_list.append(s)
            elif flag == True:
                break
        first, last = num_list[0],num_list[-1]
        head,middle,tail = file[:first],file[first:last+1],file[last+1:]
        if len(middle) < 5:
            middle = (5-len(middle))*"0"+middle
        files_list.append([head,middle,tail,index])

    return files_list

def solution(files):
    files_list=splits_files(files)
    files_list.sort(key = lambda x : (x[0],x[1],x[3]))
    answer = []
    for file in files_list:

        answer.append(files[file[3]]) #정렬은 위에서 했으니 입력 순서로 찾아서 append
    return answer

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
##["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
# print(solution(["img12.png", "img10", "img02.png", "img10.png", "IMG01.GIF", "img2.JPG"]))
# print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))