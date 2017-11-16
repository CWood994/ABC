class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1

        store = [0] * (n + 1)
        store[1] = 1
        store[2] = 2

        for i in range(3, n + 1):
            store[i] = store[i - 1] + store[i - 2]

        return store[n]

