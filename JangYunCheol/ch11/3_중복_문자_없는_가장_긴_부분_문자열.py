import collections

# "pwwkew"
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        list_s= "".join(s)

        res = set()
        map = {}
        maxcount=0
        # if 'a' not in s[0:4]:
        #     print(s[0:4])
        for char in range(len(s)):

            e= s[char]
            for point in range(0,char):
                if s[point:char] in res :
                    continue
                if s[char] in list(s[point:char]) or char-point ==0:
                    continue
                # for s[char] in res:
                res.add(s[point:char])
                map[s[point:char]] = char - point
                if s[char] in map:
                    # res.remove(str(map[max(map.keys())].key()))
                    del map[max(map.keys())]


        # return max(map.values())
        return map

        # return s

        map = {}
        max_length = start = 0
        for index, char in enumerate(s):
            if char in map and start<=map[char]:
                start = map[char] +1
            else:
                max_length = max(max_length,index - start +1)

            map[char] = index

        return max_length




s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
