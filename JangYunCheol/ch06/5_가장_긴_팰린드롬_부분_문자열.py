#p159
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        l = len(s)
        if l < 2:
            return s
        ans = [[0] * l for _ in range(l)]

        a = s[0]
        for x in range(1, l):
            for y in range(0, x):
                if x - y < 3 or ans[y + 1][x - 1]:
                    if s[x] == s[y]:
                        ans[y][x] = True
                        if len(a) <= x - y:
                            a = s[y:x + 1]
        return a

s = Solution()
print(s.longestPalindrome("babad"))

#못품