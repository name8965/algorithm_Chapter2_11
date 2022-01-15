#p190
from typing import List
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum =0
        pair=[]
        nums.sort()

        for n in nums:
            pair.append(n)
            if(len(pair)==2):
                sum+=min(pair)
                pair =[]
        return sum


s = Solution()
print(s.arrayPairSum([1,4,3,2]))


#품