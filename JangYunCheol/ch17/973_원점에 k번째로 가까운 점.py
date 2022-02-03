from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points)==1:
            return[0]
        points = self.mysort(points)
        return points[:k]



    def mysort(self,lst:List[List[int]]):
        if len(lst)==1:
            return lst


        mid = len(lst)//2
        L = lst[:mid]
        R = lst[mid:]
        return self.merge(self.mysort(L),self.mysort(R))
    def merge(self,arr1,arr2):
        l_idx=0
        r_idx=0
        result = []
        while l_idx<len(arr1) and r_idx<len(arr2):
            lsum = arr1[l_idx][0]**2+arr1[l_idx][1]**2
            rsum = arr2[r_idx][0]**2+arr2[r_idx][1]**2
            if lsum<rsum:
                result.append(arr1[l_idx])
                l_idx+=1
            else:
                result.append(arr2[r_idx])
                r_idx+=1
        if l_idx==len(arr1):
            while r_idx<len(arr2):
                result.append(arr2[r_idx])
                r_idx+=1
        else:
            while l_idx<len(arr1):
                result.append(arr1[l_idx])
                l_idx+=1

        return result


s=Solution()
print(s.kClosest([[3,3],[5,-1],[-2,4]],2))
