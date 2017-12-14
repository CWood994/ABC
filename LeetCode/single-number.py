class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        word_count = {}
        
        for i in nums:
            if i in word_count:
                if word_count[i] not in [0,1]:
                    return i
                word_count[i] += 1
            else:
                word_count[i] = 1
        
        for key, val in word_count.items():
            if val != 2:
                return key
                    