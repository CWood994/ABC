class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        my_int = 0
        _x = x if x > 0 else -x
        
        while _x != 0:
            my_int *= 10
            my_int += _x % 10
            _x /= 10
        
        my_int = my_int if my_int <= pow(2,31)-1 else 0
        return my_int if x > 0 else -my_int
        