class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        range = [0, x + 1]
        guess = sum(range) / 2

        while range[1] - range[0] > 1:
            if guess ** 2 > x:
                range[1] = guess
            else:
                range[0] = guess
            guess = sum(range) / 2

        return range[0]
