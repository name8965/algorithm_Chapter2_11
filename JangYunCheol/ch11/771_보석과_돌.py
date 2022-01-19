class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:


        j = jewels
        S = stones

        # 의식의 흐름
        count = 0

        # for char in stones:
        #     if char in jewels:
        #         count += 1
        # return count

        # 해쉬테이블(딕셔너리) 방법
        hash = {}
        count = 0

        for char in jewels:       #맵에 키와 값을 미리 할당
            hash[char] = 0

        for char in stones:
            if char in jewels:    #돌의 문자중 보석의 문자열에 존재하면 ++
                hash[char] += 1

        count += sum(hash.values()) #해쉬테이블에 들어간 값들의 합을 출력


        # #파이썬 다운 방식
        # return sum((i in jewels) for i in stones)

        return count




s = Solution()
print(s.numJewelsInStones("aA","aAAbbbb"))

