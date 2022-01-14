from curses.ascii import isalnum


class Solution:
    def isPalindrome(self, s: str) -> bool:
        #   1. 대문자를 소문자로
        #   2. 기호는 전부 삭제
        #   3. 앞글자와 뒷글자를 같은 글자
        #   4. 문자와 숫자가 포함
        #   5. 맞으면 true, 틀리면 false 값 리턴

        #   문자와 숫자(isalnum()만 빼서 소문자로 바꾸고 리스트에 저장
        l = []
        for c in s:
            if c.isalnum():
                l.append(c.lower())
        #   만약 리스트의 0번째와 -1번째가 같으면 true
        #   아니면 false 리턴
        return l == l[::-1]


s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))

#   67ms / 20.1MB
