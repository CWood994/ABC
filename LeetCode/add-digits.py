class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        while num > 9:
            temp_sum = 0
            while num > 0:
                temp_sum += num % 10
                num = num // 10
            num = temp_sum
            
        return num
        