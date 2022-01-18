import collections
from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        if s is None:
            return None
        counter =collections.Counter(s)                 # s문자열을 카운트함
        seen = set()                                    #셋 선언
        stack = []                                      #스택 리스트 선언
        #cbacdcbc c 4 b 2 a 1 d 1   a b c d
        for char in s:
            counter[char]-=1                            #카운트에서 -1해서 중복된글자가 1개이상인지 체크
            if char in seen:                            #
                continue
            while stack and char <stack[-1] and counter[stack[-1]]>0:#스택이 존재하고/ 사전식순서를 체크하며 /뒤 문자열에 존재하는지 체크
                seen.remove(stack.pop())                # 뒤에 해당 문자가 존재하므로 삭제
            stack.append(char)                          #스택에 넣기
            seen.add(char)                              #넣어진것을 확인하는용

        return ''.join(stack)








s = Solution()
print(s.removeDuplicateLetters("cbacdcbc"))
print(s.removeDuplicateLetters(""))
