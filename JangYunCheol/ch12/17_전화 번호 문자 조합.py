from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        def dfs(index,path):
            if len(path) == len(digits):
                result.append(path)
                return

            for i in range(index,len(digits)):
                for j in dic[digits[i]]:
                    dfs(i+1,path+j)
        path = ""
        dic = {"2":"abc",
               "3":"def",
               "4":"ghi",
               "5":"jkl",
               "6":"mno",
               "7":"pqrs",
               "8":"tuv",
               "9":"wxyz"}
        result = []
        dfs(0,"")

        return result

s = Solution()
print(s.letterCombinations("23"))




