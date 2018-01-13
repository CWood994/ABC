class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        temp = n
        seen = set()
        
        while temp != 1 and temp not in seen:
            seen.add(temp)
            sum = 0
            while temp > 0:
                sum += (temp%10)**2
                temp = temp // 10
            temp = sum
        
        return temp == 1
        
        