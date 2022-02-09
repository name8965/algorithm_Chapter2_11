import sys
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum = -sys.maxsize
        cur = 0
        for num in nums:
            cur = max(num,cur+num)
            best_sum = max(best_sum,cur)
        return best_sum


s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

