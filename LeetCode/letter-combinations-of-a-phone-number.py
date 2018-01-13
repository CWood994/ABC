from collections import deque

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        if digits == "":
            return []
        
        kvmaps = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        ans = deque()
        ans.append("")
        
        for i in range(len(digits)):
            while len(ans[0]) == i:
                prev = ans.popleft()
                
                for j in kvmaps[digits[i]]:
                    ans.append(prev+j)

        return list(ans)
        
        
        
            
        