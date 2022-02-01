from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # def sortmerge(intervals)
        #
        # if len(intervals)<=1:
        #     return intervals
        # lst = []
        # for i in range(len(intervals)+1):
        #
        #     sortmerge(intervals)
        #     elif not intervals[i+1]:
        #         lst.append(intervals[i])
        #     else:
        #         lst.append(intervals[i])
        #
        #
        # return lst
        # intervals.sort(key = lambda x:x[0])

        intervals.sort()
        lst = []
        for i in intervals:
            if not lst or lst[-1][1] < i[0]:
                lst.append(i)
            else:
                lst[-1][1] = max(lst[-1][1], i[1])

        return lst





s = Solution()
print(s.merge([[1,4],[0,4]]))
print(s.merge([[1,4],[5,6]]))
print(s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(s.merge([[1, 4], [4, 5]]))
print(s.merge([[1,3]]))
print(s.merge([[]]))

        # [[1, 3], [2, 6], [8, 10], [15, 18]]
        # [[1, 4], [4, 5]]