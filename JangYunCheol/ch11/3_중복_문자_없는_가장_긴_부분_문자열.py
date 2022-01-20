import collections

# "pwwkew"
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_len = 0
        map = ''

        for l in s:
            if l in map:
                map = map[map.find(l) + 1:]     #중복문자일 경우 해당 동일한 문자를 찾아서 그다음 번째부터 사용
            map += l                            #문자열에 해당 문자 추가
            if len(map) > max_len:              #최대길이가 현재 문자길이보다 크면 대입
                max_len = len(map)

        return max_len


        # return map

        # return s

        # map = {}
        # max_length = start = 0
        # for index, char in enumerate(s):
        #     if char in map and start<=map[char]:
        #         start = map[char] +1
        #     else:
        #         max_length = max(max_length,index - start +1)
        #
        #     map[char] = index
        #
        # return max_length


# "pwwkew"

s = Solution()
print(s.lengthOfLongestSubstring("abcbaccbacab"))
