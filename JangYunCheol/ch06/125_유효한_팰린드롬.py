class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. 대문자를 소문자로
        s=s.lower()
        s_list = []
        for char in s:
        # 2. 기호는 전부 삭제
        # 4. 문자와 숫자가 포함
            if char.isalnum():
                s_list.append(char)

        if len(s_list)==0:
            return True
        # 3. 앞글자와 뒷글자를 같은 글자
        if(s_list[0]!=s_list[-1]):
            return False

        while len(s_list)>1:
            if s_list.pop(0)!=s_list.pop():
                return False

        # 5. 맞으면 true, 틀리면 false 값 리턴
        return True

s = Solution()
print(s.isPalindrome(" "))







#품

















# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         # 팰린드롬 판별 및 투 포인터 확장
#         def expand(left: int, right: int) -> str:
#             while left >= 0 and right < len(s) and s[left] == s[right]:
#                 left -= 1
#                 right += 1
#             return s[left + 1:right]
#
#         # 해당 사항이 없을때 빠르게 리턴
#         if len(s) < 2 or s == s[::-1]:
#             return s
#
#         result = ''
#         # 슬라이딩 윈도우 우측으로 이동
#         for i in range(len(s) - 1):
#             result = max(result,
#                          expand(i, i + 1),
#                          expand(i, i + 2),
#                          key=len)
#         return result