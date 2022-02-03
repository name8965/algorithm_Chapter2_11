class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s= sorted(s)
        t= sorted(t)
        return s==t



s = Solution()
print(s.isAnagram("anagram","nagaram"))
print(s.isAnagram("rat","car"))