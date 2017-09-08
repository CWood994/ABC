def rev(x):
    y = 0
    while x > 0:
        y *= 10
        y += x % 10
        x = x // 10
    return y

class Solution(object):
    
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        return (rev(x) == x and x >= 0)
        
        