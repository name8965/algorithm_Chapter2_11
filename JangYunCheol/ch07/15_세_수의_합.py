#p184

from typing import List
class Solution:
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     #삼포인트 방식
    #     results = [] # 결과를 넣을 리스트
    #     nums.sort() #계산을 편하게 하기 위한 정렬                       [-4, -1, -1, 0, 1, 2]
    #     for i in range(len(nums)-2):                               # i   j   k ------->
    #         if nums[i]==nums[i-1] and i >0:# 중복되는 값 제외(결과는 같음)i       j  k----->
    #             continue
    #         for j in range(i+1,len(nums)-1):# i 의 다음번째 부터 마지막 전까지(k)
    #             if nums[j]==nums[j-1] and j>i+1:
    #                 continue
    #             for k in range(j+1,len(nums)):#j의 다음번째 부터 마지막까지
    #                 if k>j+1 and nums[k]==nums[k-1]:
    #                     continue
    #                 if nums[i] + nums[j] + nums[k] == 0:
    #                     results.append([nums[i],nums[j],nums[k]])
    #     return results



    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = [] #결과를 넣을 리스트
        nums.sort()  #계산을 편하게 해줄 정렬
        for i in range(len(nums)-2):        #중복 제거
            if nums[i]==nums[i-1] and i >0:
                continue

            left = i+1  #i 다음 번째
            right = len(nums)-1 #마지막 번째
            while left<right:
                sum=nums[i] + nums[left]+nums[right] #편한 계산을 위한 합구하기
                if(sum>0):                           #합이 0보다크면 정렬된상태로 더하는 값이 작아져야하니 right를 왼쪽으로
                    right-=1
                elif sum<0:                          #합이 0보다작으면 정렬된상태로 더하는 값이 커져야하니 left를 오른쪽으로
                    left+=1
                else:                                  #합이 0일땐 정답이므로 append
                    results.append([nums[i] , nums[left], nums[right]])
                    while left<right and nums[left]==nums[left+1]: #중복을 제거함 같은 숫자가 나올경우 같은 연산이 됨
                        left+=1
                    while left<right and nums[right]==nums[right-1]: #[-6, -3, -1, 0, 2, 4, 6]
                        right-=1
                    right-=1                                        #둘다 바꾸는 이유는 하나라도 숫자가 바뀌면 결과는 이미 0이 아님
                    left+=1                                         #어차피 다른 한쪽도 바꿔야 하므로?

        return results




s = Solution()
print(s.threeSum([-1,-1,0,1,1,2,2,-1,-5]))

-4,-1,-1,0,1,2
#품