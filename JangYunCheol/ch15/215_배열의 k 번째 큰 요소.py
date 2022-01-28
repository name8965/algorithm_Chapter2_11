import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=sorted(nums)       #오름차순 = 맨뒤가 젤큰값

        for _ in range(1,k):
            heap.pop()
        return heap.pop()

s = Solution()
print(s.findKthLargest([3,2,1,5,6,4],2))
