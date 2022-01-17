from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #   1. 문자열이 담긴 리스트
        #   2. 변환 순서는 상관 없음
        #   3. 애너그램 = 동일한 알파벳의 재배열
        #   4. 동일한 애너그램을 리스트에 넣어줌

        #   리스트의 단어를 꺼내서 알파벳이 같은지 확인
        dic = {}
        for i in range(len(strs)):
            #   단어를 재배열(in order) 하여 분리한 뒤에 합친다 (키값)
            r = ''.join(sorted(strs[i]))

            #   재배열 한 단어가 없으면 키 생성하고 값으로 들어간다.
            if r not in dic:
                dic[r] = [strs[i]]
            #   그 외의 경우 값으로 들어간다.
            else:
                dic[r].append(strs[i])

        return dic.values()


s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
