from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        result = []
        # for i in range(len(nums)):
        #     Top = nums[i]
        #     list = []
        #     list.append(nums[i])
        #     for j in range(len(nums)):
        #         if j == i:
        #             continue
        #         list.append(nums[j])
        #         for k in range(len(nums)):
        #             if k==i or k==j:
        #                 continue
        #             list.append(nums[k])
        #             result.append(list[:])
        #             list.pop()
        #         list.pop()
        dfs_result  = []
        def dfs(list):
            if not list:
                result.append(dfs_result[:])

            for i in list:
                map = list[:]
                map.remove(i)

                dfs_result.append(i)
                dfs(map)
                dfs_result.pop()
        dfs(nums)

        return  result



s = Solution()

print(s.permute([1,2,3]))