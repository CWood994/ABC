# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        lo = 1
        hi = n
        
        while lo < hi:
            mi = (lo + hi) // 2
            if isBadVersion(mi):
                hi = mi
            else:
                lo = mi + 1
        
        return lo
