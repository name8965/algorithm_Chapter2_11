from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not len(matrix) or not len(matrix[0]):
            return False
        lst = []
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[i])):
        #        lst.append(matrix[i][j])
        #
        # print(lst)
        h= len(matrix)
        w= len(matrix[0])
        y = h-1
        x = 0
        while not(y<0 or x>=w):
            cur = matrix[y][x]

            if target<cur:
                y-=1
            elif target>cur:
                x+=1
            else:
                return True
        return False



    def binary_search(nums, target):
        def bs(start, end):
            if start > end:
                return -1

            mid = (start + end) // 2

            if nums[mid] < target:
                return bs(mid + 1, end)
            elif nums[mid] > target:
                return bs(start, mid - 1)
            else:
                return mid
        return bs(0, len(nums) - 1)



s= Solution()
print(s.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],20))