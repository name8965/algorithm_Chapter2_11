from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        #   reverse 함수 사용
        s.reverse()


s1 = Solution()
print(s1.reverseString(["h", "e", "l", "l", "o"]))
