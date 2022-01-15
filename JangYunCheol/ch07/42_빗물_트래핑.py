from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:      #예외 처리
            return 0
        leftmax,rightmax = [],[]    #각 최대치 리스트 선언
        result =0

        leftmax.append(height[0])   #초기값 비교를 위한
        for i in range(1,len(height)):
            leftmax.append(max(height[i],leftmax[i-1])) #이전 Left에 가장 높은 값과 높이를 비교해서 max값 반환(가장 큰값)
        rightmax = [0] * len(height) #초기값 설정을 위한 공간 할당(오른쪽부터 오기때문)
        rightmax[len(height)-1] = height[len(height)-1] #위와 동일
        for i in reversed(range(len(height)-1)):    #reversed로 포문을 거꾸로 돌림
            rightmax[i]=(max(height[i],rightmax[i+1]))  #오른쪽 맥스값과 높이중 더 큰 값을 할당
            #append?
        for i in range(len(height)-1):
            result += min(leftmax[i],rightmax[i])-height[i] #오른쪽/왼쪽의 높이중 겹치는 부분 = 교집합= min 을 이용해서 구하고
                                                            #높이(height)의 경우는 차오르지 않으니 제외
        return result





s=Solution()
print(s.trap([0,1,0,1,0,3,0,1,0,1,0]))

print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))

#품