class Solution:
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        
        # dp[i][j] is max len ending at A[i] and B[j]
        dp = []
        for _ in range(len(B)+1):
            dp.append([0]*(len(A)+1))
        
        res = 0
        for i in range(len(A)+1):
            for j in range(len(B)+1):
                if i == 0 or j == 0:
                    continue
                elif A[i-1] == B[j-1]:
                    tmp = 1 + dp[i-1][j-1]
                    dp[i][j] = tmp
                    res = max(res, tmp)
        return res

        
        