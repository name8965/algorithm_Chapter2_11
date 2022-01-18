
def is_valid(s):
    if not(len(s)>=2 and len(s)<=50):
        return "No"
    # s=s.strip('\n')
    pair ={")":"("}

    opener = "("
    stack = []

    for char in s:
        if char in opener:
            stack.append(char)
        else:
            if not stack:
                return "No"
            top = stack.pop()

            if pair[char]!=top:
                return "No"
    return "No" if stack else "Yes"

import sys


T = int(sys.stdin.readline())   # 입력받을 숫자

for i in range(T):
    VPS = sys.stdin.readline().rstrip()
    print(is_valid(VPS))

# print(is_valid("(())())"))
# print(is_valid("(((()())()"))
# print(is_valid("(()())((()))"))
# print(is_valid("((()()(()))(((())))()"))
# print(is_valid("()()()()(()()())()"))
# print(is_valid("(()((())()("))
# print('예시2')
# print(is_valid("(("))
# print(is_valid("))"))
# print(is_valid("())(()"))