import collections
import re
from typing import List
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        delet = ".,!;"
        for char in range(len(delet)):
            paragraph = paragraph.replace(delet[char], "").lower()
        # words = [word for word in re.sub(r'[^\w]',' ',paragraph).lower().split() if word not in banned]

        result = paragraph.split(' ')
        mapresult= collections.Counter(result)
        maxvalue=0
        check = False
        for k,v in mapresult.items():
            for ben in banned:
                if k!=ben and (v>maxvalue or v==maxvalue):
                    check = True
                    maxkey = k
                    maxvalue = v
        if check ==False:
            maxvalue=1
            maxkey = [k for k, v in mapresult.items() if v == maxvalue]
            maxkey = " ".join(maxkey)
        # return maxkey

        return mapresult





s = Solution()

# print(s.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.",["hit"]))
# print(s.mostCommonWord("a.",[]))
# print(s.mostCommonWord("Bob. hIt, baLl",["bob", "hit"]))
print(s.mostCommonWord("a, a, a, a, b,b,b,c, c",["a"]))


#못품