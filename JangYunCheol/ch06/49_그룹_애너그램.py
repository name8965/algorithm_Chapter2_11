import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)

        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
            print(anagrams)
        return list(anagrams.values())



s=Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print('test')

#품