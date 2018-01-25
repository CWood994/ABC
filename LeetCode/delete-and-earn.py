class Solution:
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        counts = [0] * 10001
        
        for n in nums:
            counts[n] += n
            
        takei = counts[0]
        skipi = 0     
        for i in range(1,len(counts)):
            tmp = takei
            takei = skipi + counts[i]
            skipi = max(skipi, tmp)
            
        return max(takei, skipi)
        
    