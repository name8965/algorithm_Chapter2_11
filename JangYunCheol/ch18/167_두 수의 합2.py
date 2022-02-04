import bisect
from typing import List


# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:#[2,7,11,15],13
#         lst = []
#         idx = bisect.bisect_left(numbers,target)
#         i=0
#         while True:
#             if idx+i==len(numbers):
#                 i+=1
#                 continue
#             cur = target-(numbers[idx-i])
#             result = bisect.bisect_left(numbers,cur)
#             if result<len(numbers) and numbers[result] == cur:
#                 a = (result+1)
#                 if a<0:
#                     a=(result+1)%len(numbers)
#                 lst.append(a)
#                 break
#             else:
#                 i+=1
#         a =idx-i+1
#         if a<0:
#             a=a%len(numbers)
#         if a in lst:
#             a+=1
#         lst.append(a)
#
#         return sorted(lst)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:#[2,7,11,15],18
        if len(numbers) == 2:
            return [1, 2]
        lst = []
        idx = bisect.bisect_left(numbers,target)
        if idx < len(numbers) and numbers[idx] == target:
            for i in range(len(numbers)):
                if numbers[i] == 0 and idx!=i:
                    return sorted([idx+1,i+1])
        if numbers[idx-1]<0:
            a= target+numbers[idx-1]
            a *=-1
            b= numbers.index(a)
            return sorted([idx,b+1])


        lst = numbers[:idx].copy()
        i = len(lst)-1
        if len(lst) ==2:
            return [1,2]
        for i,j in enumerate(lst):
            sumtarget = target- j
            idx2 = bisect.bisect_left(lst,sumtarget)
            if idx2 < len(lst) and lst[idx2] == sumtarget:
                return i+1,idx2+1



def binarytest(nums,target):
    idx = bisect.bisect_left(nums,target)
    return idx

# print(binarytest([2,3,4,7],6))
s=Solution()
# # print(s.twoSum([-1,0],-1))
# print(s.twoSum([2,3,4],6))
# print(s.twoSum([-1,-1,1,1],-2))
# print(s.twoSum([12,13,23,28,43,44,59,60,61,68,70,86,88,92,124,125,136,168,173,173,180,199,212,221,227,230,277,282,306,314,316,321,325,328,336,337,363,365,368,370,370,371,375,384,387,394,400,404,414,422,422,427,430,435,457,493,506,527,531,538,541,546,568,583,585,587,650,652,677,691,730,737,740,751,755,764,778,783,785,789,794,803,809,815,847,858,863,863,874,887,896,916,920,926,927,930,933,957,981,997],542))
print(s.twoSum([2,7,11,15],13))
# print(s.twoSum([-1,0],-1))
# print(s.twoSum([-3,3,6,8],0))
# print(s.twoSum([0,0,3,4],0))
# print(s.twoSum([1,3,4,4],8))