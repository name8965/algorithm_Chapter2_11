from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0
        end = len(nums)-1

        flag = False
        for i in range(1,len(nums)):
            if nums[i-1]!=nums[i]:
                flag=True
                break
        if not flag:
            return
        i=0
        if i==end:
            return
        while i<=end:
            if nums[i] == 0:

                nums[i],nums[start] = nums[start],nums[i]
                start+=1
            elif nums[i]==2:

                nums[i],nums[end]=nums[end],nums[i]
                end-=1
                continue
            i+=1




s = Solution()
tc1 = [2,0,2,1,1,0]
tc2 = [2,0,1]
tc3 = [0,0]
s.sortColors(tc1)
print(tc1)
s.sortColors(tc2)
print(tc2)
