from typing import List

class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        if not temp:
            return temp     #악질 예제 예외처리

        result = [0] * len(temp)                            #입력된 리스트의 크기 만큼 공간 할당
        stack = []                                          # 스택용으로 쓸 리스트 선언
        for cur_day,t in enumerate(temp):                   # 입력만큼 포문
            while stack and temp[stack[-1]]<t:              # 스택의 마지막인덱스의 입력값 리스트의 값이 t보다 작은지
                prv_day = stack.pop()                       # pop 인덱스 추출
                result[prv_day] =   cur_day-prv_day         # 해당 인덱스로 날짜(인덱스)차이를 결과로내보냄
            stack.append(cur_day)                           # 매 포문마다 스택을 넣어줌


        return result
        #
        # result = [0] * len(temp)
        #
        # for i in range(len(temp)-1):
        #     for j in range(i+1,len(temp)):
        #         if temp[j]>temp[i]:
        #             result[i] = j-i
        #             break
        #
        # return result


s = Solution()
print(s.dailyTemperatures([73,74,75,71,69,72,76,73]))
print(s.dailyTemperatures([30,40,50,60]))
print(s.dailyTemperatures([]))