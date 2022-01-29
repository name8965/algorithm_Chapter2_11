from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not nums:
            return ""

        for i in range(1,len(nums)):
            for j in range(1,i+1):
                cur = i-j
                if str(nums[cur])+str(nums[cur+1])<str(nums[cur+1])+str(nums[cur]):
                    nums[cur],nums[cur+1] = nums[cur+1],nums[cur]
                else:
                    break


        return str(int(''.join(str(_) for _ in nums)))



s = Solution()
print(s.largestNumber([10,2]))
print(s.largestNumber([3,30,34,5,9]))
print(s.largestNumber([0,0]))