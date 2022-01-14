#p159
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s[::-1]==s or len(s)<2:
            return s

        for i in range(0,len(s)-1):
            print(0,len(s)-1)

        return "test"

s = Solution()
print(s.longestPalindrome("babad"))

#못품